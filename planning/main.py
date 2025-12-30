import argparse
import sys
import os

# Ensure we can import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llm import OllamaLLM
from planner import PlannerAgent
from executor import ExecutorAgent

def main():
    parser = argparse.ArgumentParser(description="Run the Planning Agent")
    parser.add_argument("task", help="The complex task to execute")
    parser.add_argument("--ollama-url", type=str, default="http://localhost:11434", help="Ollama URL")
    
    args = parser.parse_args()

    print(f"Initializing Agents with Ollama at {args.ollama_url}")
    llm = OllamaLLM(base_url=args.ollama_url, model="llama3.2")
    planner = PlannerAgent(llm)
    executor = ExecutorAgent(llm)
    
    # 1. Plan
    print("\n--- PHASE 1: PLANNING ---")
    plan = planner.create_plan(args.task)
    print("Generated Plan:")
    for i, step in enumerate(plan):
        print(f"{i+1}. {step}")

    # 2. Execute
    print("\n--- PHASE 2: EXECUTION ---")
    context = ""
    for i, step in enumerate(plan):
        print(f"\n[Executing Step {i+1}]: {step}")
        result = executor.execute_step(step, context)
        print(f"Result: {result}")
        context += f"Step {i+1}: {step}\nResult: {result}\n\n"

    # 3. Final Summary (Optional: could have a summarizer agent)
    print("\n" + "="*50)
    print("FINAL EXECUTION COMPLETE")
    print("="*50)
    print("See execution log above for details.")

if __name__ == "__main__":
    main()
