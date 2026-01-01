# Planning Pattern Agent Demo

This application demonstrates the **Planning (Plan-and-Execute)** pattern for Agentic AI.
A **Planner Agent** breaks down a complex query into sequential steps, and an **Executor Agent** executes them using available tools.

## Components

- `main.py`: Orchestrator (CLI).
- `planner.py`: Generates the step-by-step plan.
- `executor.py`: Executes steps using tools and maintains context.
- `tools.py`: Tools (DuckDuckGo MCP server, Calculator).
- `llm.py`: Interface to Ollama.
- `docker-compose.yml`: Runs the app + Ollama.

## Usage with Docker Compose

```bash
cd planning
docker compose up --build
```

### What happens?
1.  **Ollama** starts and pulls `gemma3:1b`.
2.  **App** runs the default query: "What is the total population of the United States of America as of December 2025?"
3.  **Phase 1 (Planning)**: The Planner agent outlines the steps.
4.  **Phase 2 (Execution)**: The Executor agent performs each step, passing results to the next.

### Custom Query
To run a specific query:

```bash
docker compose run app "Who is the CEO of Tesla and what is his or her net worth?" --ollama-url http://ollama:11434
```
