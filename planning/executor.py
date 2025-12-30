from llm import OllamaLLM
from tools import TOOLS
import re

class ExecutorAgent:
    def __init__(self, llm: OllamaLLM):
        self.llm = llm
        self.tools = {t.name: t for t in TOOLS}

    def execute_step(self, step: str, context: str) -> str:
        tool_names = ', '.join([t.name for t in self.tools.values()])
        tool_descriptions = '\n'.join([f'{t.name}: {t.description}' for t in self.tools.values()])
        
        prompt = (
            f"You are an Executor Agent.\n"
            f"Your job is to execute the following step using the available tools.\n"
            f"You have access to the following context from previous steps:\n"
            f"{context}\n\n"
            f"Available Tools: {tool_names}\n"
            f"Tool Descriptions:\n"
            f"{tool_descriptions}\n\n"
            f"Current Step: {step}\n\n"
            f"To use a tool, output: Action: ToolName[Input]\n"
            f"If you have the answer directly or after using a tool, output: Final Answer: [Answer]\n"
            f"Think step-by-step."
        )

        response = self.llm.generate(prompt)
        
        # Simple ReAct-like parsing (simplified for demo)
        # Look for "Action: Name[Input]"
        action_match = re.search(r"Action: (\w+)\[(.*?)\]", response)
        if action_match:
            tool_name = action_match.group(1)
            tool_input = action_match.group(2)
            
            if tool_name in self.tools:
                result = self.tools[tool_name].run(tool_input)
                return f"Used {tool_name}('{tool_input}'). Result: {result}"
            else:
                return f"Error: Tool {tool_name} not found."
        
        # Look for Final Answer
        final_match = re.search(r"Final Answer: (.*)", response, re.DOTALL)
        if final_match:
            return final_match.group(1).strip()

        # Fallback if no structured action or answer found
        return response
