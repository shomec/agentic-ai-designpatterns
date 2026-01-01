import argparse
import sys
import os

# Ensure we can import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llm import OllamaLLM
from agents import ResearcherAgent, WriterAgent, EditorAgent, PublisherAgent, SentimentAnalyzerAgent

def main():
    parser = argparse.ArgumentParser(description="Run the Multi-Agent Content Team")
    parser.add_argument("topic", help="The topic to create content about")
    parser.add_argument("--ollama-url", type=str, default="http://localhost:11434", help="Ollama URL")
    
    args = parser.parse_args()

    print(f"Initializing Agents with Ollama at {args.ollama_url}")
    llm = OllamaLLM(base_url=args.ollama_url, model="gemma3:1b")
    
    researcher = ResearcherAgent(llm)
    writer = WriterAgent(llm)
    editor = EditorAgent(llm)
    publisher = PublisherAgent(llm)
    analyzer = SentimentAnalyzerAgent(llm)
    
    print("\n" + "="*50)
    print(f"STARTING WORKFLOW FOR TOPIC: {args.topic}")
    print("="*50)
    
    # Step 1: Research
    print("\n[Researcher (Alice)]: Starting research...")
    research_summary = researcher.perform_research(args.topic)
    print(f"\n[Researcher (Alice)]: Research complete.\nSummary:\n{research_summary}\n")
    
    # Step 2: Write
    print("\n[Writer (Bob)]: Drafting content...")
    draft = writer.write_draft(args.topic, research_summary)
    print(f"\n[Writer (Bob)]: Draft complete.\n\n--- DRAFT ---\n{draft}\n-------------\n")

    # Step 3: Review
    print("\n[Editor (Charlie)]: Reviewing draft...")
    critique = editor.review_draft(draft)
    print(f"\n[Editor (Charlie)]: Review complete.\nCritique:\n{critique}\n")

    # Step 4: Publish
    print("\n[Publisher (Dave)]: Publishing content...")
    final_publication = publisher.publish_content(draft)
    print(f"\n[Publisher (Dave)]: Publication Released.\n\n--- PUBLICATION ---\n{final_publication}\n-------------------\n")

    # Step 5: Sentiment Analysis
    print("\n[Sentiment Analyzer (Eve)]: Analyzing reader sentiment...")
    analysis = analyzer.analyze_sentiment(final_publication)
    print(f"\n[Sentiment Analyzer (Eve)]: Analysis complete.\nReaction:\n{analysis}\n")

    print("\n" + "="*50)
    print("WORKFLOW COMPLETE")
    print("="*50)

if __name__ == "__main__":
    main()
