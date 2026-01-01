import os
from abc import ABC, abstractmethod
import random
import json
import urllib.request
import urllib.error

class AbstractLLM(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generates a response based on the given prompt.
        """
        pass

class MockLLM(AbstractLLM):
    """
    A mock LLM that returns deterministic responses for demonstration purposes.
    It simulates a bad initial draft and a good critique.
    """
    def generate(self, prompt: str) -> str:
        # Check if the prompt is asking for a draft (Generator) or a critique (Reflector)
        if "Review the following output" in prompt:
            # This is the reflector/critic
            return (
                "Critique:\n"
                "1. The code lacks error handling.\n"
                "2. The variable names are not descriptive.\n"
                "3. It doesn't handle edge cases like n <= 0.\n"
                "Recommendation: Rewrite with type hints, better variable names, and input validation."
            )
        else:
            # This is the generator
            # If the prompt contains "Recommendation:", it means we are in the second pass (final generation)
            if "Recommendation:" in prompt:
                return (
                    "```python\n"
                    "def fibonacci(n: int) -> int:\n"
                    "    \"\"\"Calculates the nth Fibonacci number.\"\"\"\n"
                    "    if n < 0:\n"
                    "        raise ValueError('Input must be non-negative')\n"
                    "    elif n == 0:\n"
                    "        return 0\n"
                    "    elif n == 1:\n"
                    "        return 1\n"
                    "    else:\n"
                    "        a, b = 0, 1\n"
                    "        for _ in range(2, n + 1):\n"
                    "            a, b = b, a + b\n"
                    "        return b\n"
                    "```"
                )
            else:
                # Initial draft (bad code)
                return (
                    "def fib(n):\n"
                    "    if n==1: return 1\n"
                    "    if n==0: return 0\n"
                    "    return fib(n-1)+fib(n-2)"
                )

class OllamaLLM(AbstractLLM):
    """
    Implementation for local Ollama API.
    Defaults to http://localhost:11434
    """
    def __init__(self, model="llama3", base_url="http://localhost:11434"):
        self.model = model
        self.base_url = base_url

    def generate(self, prompt: str) -> str:
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.5,
                "repeat_penalty": 1.1,
                "top_p": 0.9,
                "top_k": 40
            }
        }
        
        try:
            data = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req) as response:
                response_data = json.loads(response.read().decode("utf-8"))
                return response_data.get("response", "").strip()
        except urllib.error.URLError as e:
            return f"Error communicating with Ollama: {e}. Ensure Ollama is running at {self.base_url}"

