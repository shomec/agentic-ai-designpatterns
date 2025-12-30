# Reflection Pattern Agentic AI Demo

This repository demonstrates the **Reflection Pattern** in Agentic AI using Python.
The application mimics an agent that generates an initial draft, reflects on it (critique), and then produces an improved final version.

## structure

- `main.py`: CLI entry point.
- `workflow.py`: Logic for the reflection loop.
- `agents.py`: Generator and Reflector agent implementations.
- `llm.py`: Abstract LLM interface with `MockLLM` (default) and `OpenAILLM`.
- `prompts.py`: System prompts.

## Usage

### 1. Run with Mock LLM (Default)
Run the application without any API keys to see the pattern in action.

```bash
python3 reflection/main.py "Write a python script to calculate fibonacci"
```

### 2. Run with Ollama
To use a local Ollama instance (default: `http://localhost:11434`), use the `--use-ollama` flag.

```bash
python3 reflection/main.py "Write a python script to calculate fibonacci" --use-ollama
```

You can also specify the model (default: `llama3`):

```bash
python3 reflection/main.py "Write a python script to calculate fibonacci" --use-ollama --model mistral
```

```bash
python3 reflection/main.py "Write a python script to calculate fibonacci" --use-ollama --model mistral
```

### 3. Run with Docker Compose
To run the entire stack (Application + Ollama) using Docker Compose:

```bash
cd reflection
docker compose up --build
```

This will:
1. Start an Ollama container.
2. Build and start the Python application container.
3. The app will automatically connect to Ollama and run the demo task.

## How it works


1. **Generation**: The agent creates an initial draft based on the task.
2. **Reflection**: A separate "Reflector" agent reviews the draft and provides a critique.
3. **Improvement**: The first agent uses the critique to generate a better final version.
