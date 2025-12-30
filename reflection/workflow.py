from .agents import GeneratorAgent, ReflectorAgent

class ReflectionWorkflow:
    def __init__(self, generator: GeneratorAgent, reflector: ReflectorAgent):
        self.generator = generator
        self.reflector = reflector

    def run(self, task: str) -> dict:
        print(f"--- Starting Reflection Workflow for task: '{task}' ---")
        
        # Step 1: Generate Initial Draft
        print("\n[1] Generating Initial Draft...")
        draft = self.generator.generate_draft(task)
        print(f"Draft generated ({len(draft)} chars).")

        # Step 2: Reflect on the Draft
        print("\n[2] Reflecting on Draft...")
        critique = self.reflector.reflect(task, draft)
        print("Critique generated.")

        # Step 3: Improve based on Critique
        print("\n[3] Generating Improved Version...")
        final_version = self.generator.generate_improved(task, critique)
        print(f"Final version generated ({len(final_version)} chars).")

        return {
            "task": task,
            "draft": draft,
            "critique": critique,
            "final_version": final_version
        }
