import argparse
import sys
import os

# Ensure we can import modules from the current directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reflection.llm import MockLLM, OllamaLLM
from reflection.agents import GeneratorAgent, ReflectorAgent
from reflection.workflow import ReflectionWorkflow

def main():
    parser = argparse.ArgumentParser(description="Run the Reflection Pattern Agentic AI Demo")
    parser.add_argument("task", help="The task for the agent to perform")
    parser.add_argument("--use-ollama", action="store_true", help="Use Ollama instead of Mock LLM")
    parser.add_argument("--model", type=str, default="gemma3:1b", help="Model to use for Ollama (default: gemma3:1b)")
    parser.add_argument("--ollama-url", type=str, default="http://localhost:11434", help="Ollama API URL (default: http://localhost:11434)")
    
    args = parser.parse_args()

    # Choose LLM Provider
    if args.use_ollama:
        print(f"Using Ollama LLM with model: {args.model} at {args.ollama_url}")
        llm = OllamaLLM(model=args.model, base_url=args.ollama_url)
    else:
        print("Using Mock LLM for demonstration.")
        llm = MockLLM()

    # Initialize Agents
    generator = GeneratorAgent(llm)
    reflector = ReflectorAgent(llm)

    # Initialize and Run Workflow
    workflow = ReflectionWorkflow(generator, reflector)
    result = workflow.run(args.task)

    # Print Results
    print("\n" + "="*50)
    print("FINAL RESULTS")
    print("="*50)
    
    print("\n\n--- INITIAL DRAFT ---")
    print(result["draft"])
    
    print("\n\n\n\n--- CRITIQUE ---")
    print(result["critique"])
    
    print("\n\n\n\n--- FINAL VERSION ---")
    print(result["final_version"])
    print("\n" + "="*50)

if __name__ == "__main__":
    main()
