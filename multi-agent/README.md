# Multi-Agent Content Team

This application demonstrates the **Multi-Agent** pattern, where specialized agents collaborate to complete a task.

## The Team
1.  **Researcher (Alice)**: Uses `mcp/duckduckgo` to gather real-world information on a topic.
2.  **Writer (Bob)**: Takes the research summary and drafts a blog post.
3.  **Editor (Charlie)**: Reviews the draft and provides a critique (similar to the Reflection pattern).
4.  **Publisher (Dave)**: Formats and "publishes" the approved content.
5.  **Sentiment Analyzer (Eve)**: Reads the publication and assigns a sentiment score (1-5) and reaction.

## Components
- `main.py`: Orchestrator (CLI).
- `agents.py`: Defines the specific agent roles using the base `Agent` class.
- `tools.py`: Connects to MCP servers (DuckDuckGo).
- `docker-compose.yml`: Runs the app, Ollama, and mounts `docker.sock` for MCP.

## Usage

```bash
cd multi-agent
docker compose up --build
```

### Custom Topic
To run with a different topic:

```bash
docker compose run app "The impact of Quantum Computing on Cryptography" --ollama-url http://ollama:11434
```
