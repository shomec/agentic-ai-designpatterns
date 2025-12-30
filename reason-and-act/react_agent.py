from llm import OllamaLLM
from tools import TOOLS, Tool
import re

REACT_PROMPT_TEMPLATE = """Answer the following questions as best you can. You have access to the following tools:

{tool_desc}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {question}
"""

class ReActAgent:
    def __init__(self, llm: OllamaLLM):
        self.llm = llm
        self.tools = {t.name: t for t in TOOLS}

    def _build_prompt(self, question, scratchpad):
        tool_desc = "\\n".join([f"{t.name}: {t.description}" for t in self.tools.values()])
        tool_names = ", ".join(self.tools.keys())
        prompt = REACT_PROMPT_TEMPLATE.format(
            tool_desc=tool_desc,
            tool_names=tool_names,
            question=question
        )
        return prompt + scratchpad

    def run(self, question):
        scratchpad = ""
        max_steps = 10
        print(f"--- Starting ReAct Agent ---")
        
        for i in range(max_steps):
            prompt = self._build_prompt(question, scratchpad)
            
            # Stop generation at "Observation:" so the LLM doesn't hallucinate the result
            response = self.llm.generate(prompt, stop="Observation:")
            response = response.strip()
            
            print(f"\n[Step {i+1}]")
            print(response)

            scratchpad += response + "\n"

            # Check for Final Answer
            if "Final Answer:" in response:
                return response.split("Final Answer:")[-1].strip()

            # Parse Action
            # Regex to find "Action: <name>" and "Action Input: <input>"
            action_match = re.search(r"Action: (.*?)[\n\r]+Action Input: (.*)", response, re.DOTALL)
            
            if action_match:
                tool_name = action_match.group(1).strip()
                tool_input = action_match.group(2).strip()
                
                if tool_name in self.tools:
                    print(f"-> Executing {tool_name} with input: {tool_input}")
                    observation = self.tools[tool_name].run(tool_input)
                    print(f"-> Observation: {observation}")
                    
                    scratchpad += f"Observation: {observation}\n"
                else:
                    obs = f"Error: Tool '{tool_name}' not found."
                    print(f"-> {obs}")
                    scratchpad += f"Observation: {obs}\n"
            else:
                # If the LLM didn't follow format, maybe it's just thinking or finished without label.
                # In a robust system, we'd handle this better.
                print("-> No action parsed. Terminating or retrying...")
                scratchpad += "Observation: Please provide an Action and Action Input, or a Final Answer.\n"
        
        return "Agent stopped due to max steps."
