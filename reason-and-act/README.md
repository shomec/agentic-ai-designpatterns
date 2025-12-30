# Reason and Act (ReAct) Agent Demo

This application demonstrates the **ReAct (Reason + Act)** pattern for Agentic AI.
The agent receives a query, reasons about it, uses tools (like Search or Calculator), and iterates until it finds an answer.

## Components

- `main.py`: CLI Entry point.
- `react_agent.py`: Implements the ReAct loop (Thought -> Action -> Observation).
- `tools.py`: Tools (DuckDuckGo MCP server, Calculator).
- `llm.py`: Interface to Ollama.
- `docker-compose.yml`: Runs the app + Ollama.

## Usage with Docker Compose

This is the recommended way to run the application as it handles the Ollama dependency automatically.

```bash
cd reason-and-act
docker compose up --build
```

### What happens?
1.  **Ollama** service starts.
2.  **init-ollama** service waits for Ollama to be ready and pulls the `llama3.2` model.
3.  **app** service runs the default query: "Research Apple's latest quarterly revenue and compare it to Google's and Microsoft's."
    - It uses the ReAct agent to reason, calling the Search tool to find revenue data for both companies.
    - It compares the findings and provides a final answer.

### Custom Query
To run a specific query, you can override the command in `docker-compose.yml` or run:

```bash
docker compose run app "What is the stock price of Apple?" --ollama-url http://ollama:11434
```
