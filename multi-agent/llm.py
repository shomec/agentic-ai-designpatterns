import json
import urllib.request
import urllib.error

class OllamaLLM:
    """
    Implementation for local Ollama API.
    Defaults to http://localhost:11434
    """
    def __init__(self, model="llama3.2", base_url="http://localhost:11434"):
        self.model = model
        self.base_url = base_url

    def generate(self, prompt: str, stop=None) -> str:
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }
        if stop:
            payload["stop"] = stop

        try:
            data = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req) as response:
                response_data = json.loads(response.read().decode("utf-8"))
                return response_data.get("response", "")
        except urllib.error.URLError as e:
            return f"Error communicating with Ollama: {e}. Ensure Ollama is running at {self.base_url}"
