from llm import OllamaLLM

class PlannerAgent:
    def __init__(self, llm: OllamaLLM):
        self.llm = llm

    def create_plan(self, task: str):
        prompt = (
            f"You are a Planner Agent.\n"
            f"Your job is to break down the following complex task into a sequence of simple, numbered steps that can be executed by another agent.\n"
            f"Each step should be a self-contained instruction.\n"
            f"Do not respond with anything other than the numbered list of steps.\n\n"
            f"Task: {task}\n\n"
            f"Plan:"
        )
        response = self.llm.generate(prompt)
        
        # Parse the response into a list of steps
        steps = []
        for line in response.split('\n'):
            line = line.strip()
            if line and (line[0].isdigit() or line.startswith('-')):
                # Remove numbering like "1. " or "- "
                # Very basic parsing
                cleaned_step = line.lstrip('0123456789.- ').strip()
                if cleaned_step:
                    steps.append(cleaned_step)
        
        return steps
