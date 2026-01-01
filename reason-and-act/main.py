import argparse
import sys
import os

# Ensure we can import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llm import OllamaLLM
from react_agent import ReActAgent

def main():
    parser = argparse.ArgumentParser(description="Run the ReAct Agent")
    parser.add_argument("question", help="The question to answer")
    parser.add_argument("--ollama-url", type=str, default="http://localhost:11434", help="Ollama URL")
    
    args = parser.parse_args()

    print(f"Initializing Agent with Ollama at {args.ollama_url}")
    llm = OllamaLLM(base_url=args.ollama_url, model="gemma3:1b")
    agent = ReActAgent(llm)
    
    final_answer = agent.run(args.question)
    
    print("\n" + "="*50)
    print("FINAL ANSWER")
    print("="*50)
    print(final_answer)

if __name__ == "__main__":
    main()
