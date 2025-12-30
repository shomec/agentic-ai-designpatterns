from .llm import AbstractLLM
from .prompts import GENERATOR_SYSTEM_PROMPT, REFLECTION_SYSTEM_PROMPT

class Agent:
    def __init__(self, llm: AbstractLLM, system_prompt: str):
        self.llm = llm
        self.system_prompt = system_prompt

    def run(self, user_input: str) -> str:
        # In a real system, we would construct a proper message history.
        # Here we just concatenate for simplicity in the Mock/Simple setup.
        full_prompt = f"{self.system_prompt}\n\nUser: {user_input}"
        return self.llm.generate(full_prompt)

class GeneratorAgent(Agent):
    def __init__(self, llm: AbstractLLM):
        super().__init__(llm, GENERATOR_SYSTEM_PROMPT)

    def generate_draft(self, task: str) -> str:
        return self.run(task)

    def generate_improved(self, task: str, critique: str) -> str:
        prompt = (
            f"Original Task: {task}\n"
            f"Critique & Recommendation: {critique}\n"
            "Please generate an improved version of the response based on the recommendation."
        )
        return self.run(prompt)

class ReflectorAgent(Agent):
    def __init__(self, llm: AbstractLLM):
        super().__init__(llm, REFLECTION_SYSTEM_PROMPT)

    def reflect(self, task: str, draft: str) -> str:
        prompt = (
            f"Original Task: {task}\n"
            f"Draft Response to Review:\n{draft}\n"
            "Review the following output and check for errors, style, and completeness."
        )
        return self.run(prompt)
