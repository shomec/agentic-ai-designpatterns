from llm import OllamaLLM
from tools import TOOLS_RESEARCHER
import re

class Agent:
    def __init__(self, name, role, goal, llm: OllamaLLM):
        self.name = name
        self.role = role
        self.goal = goal
        self.llm = llm

    def generate_reply(self, message: str, context: str = "") -> str:
        prompt = (
            f"You are {self.name}, a {self.role}.\n"
            f"Your Goal: {self.goal}\n\n"
            f"Context: {context}\n\n"
            f"Task/Message: {message}\n\n"
            f"Response:"
        )
        return self.llm.generate(prompt)

class ResearcherAgent(Agent):
    def __init__(self, llm: OllamaLLM):
        super().__init__("Alice", "Researcher", "Gather accurate information about the requested topic.", llm)
        self.tools = {t.name: t for t in TOOLS_RESEARCHER}

    def perform_research(self, topic: str) -> str:
        # Simple ReAct-like one-shot for research
        prompt = (
            f"You are a Researcher.\n"
            f"Topic: {topic}\n"
            f"Available Tools: Search\n"
            f"To use search, output strictly: Action: Search[Query]\n"
            f"After you have the info, summarize it."
        )
        # In a real loop we would parse and loop. For simplicity, we hardcode a search step.
        # Let's just create a search query based on the topic first.
        
        search_query_prompt = f"Generate a search query for the topic: {topic}. Output ONLY the query."
        query = self.llm.generate(search_query_prompt).strip().strip('"')
        
        print(f"[{self.name}] Searching for: {query}")
        search_result = self.tools["Search"].run(query)
        
        summary_prompt = (
            f"Summarize the following search results for the topic '{topic}':\n"
            f"{search_result}\n\n"
            f"Summary:"
        )
        summary = self.llm.generate(summary_prompt)
        return summary

class WriterAgent(Agent):
    def __init__(self, llm: OllamaLLM):
        super().__init__("Bob", "Writer", "Write compelling content based on research.", llm)

    def write_draft(self, topic: str, research_summary: str) -> str:
        return self.generate_reply(
            f"Write a blog post about '{topic}' using the following research.",
            context=f"Research Summary:\n{research_summary}"
        )

class EditorAgent(Agent):
    def __init__(self, llm: OllamaLLM):
        super().__init__("Charlie", "Editor", "Review content for clarity, accuracy, and style.", llm)

    def review_draft(self, draft: str) -> str:
        return self.generate_reply(
            f"Critique the following draft. Provide constructive feedback.",
            context=f"Draft:\n{draft}"
        )

class PublisherAgent(Agent):
    def __init__(self, llm: OllamaLLM):
        super().__init__("Dave", "Publisher", "Format and publish approved content.", llm)

    def publish_content(self, content: str) -> str:
        return self.generate_reply(
            "Format the following content as a final official publication. Add a title and standard formatting.",
            context=f"Approved Content:\n{content}"
        )

class SentimentAnalyzerAgent(Agent):
    def __init__(self, llm: OllamaLLM):
        super().__init__("Eve", "Sentiment Analyzer", "Analyze reader sentiment.", llm)

    def analyze_sentiment(self, content: str) -> str:
        return self.generate_reply(
            "Read the following publication. Simulate a reader's perspective. Provide a sentiment score on a scale of 1 to 5 (where 5 is best) and a brief explanation of the reaction.",
            context=f"Published Content:\n{content}"
        )
