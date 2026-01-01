# Agentic AI Design Patterns

Welcome to the **Agentic AI Design Patterns** repository. This project showcases various "Agentic AI" design patterns popularized by [DeepLearning.AI](https://www.deeplearning.ai/), featuring functional demos of autonomous, iterative, and collaborative agentic AI applications. The code in this repository was developed with the assistance of **Google AntiGravity**.

Instead of expecting an LLM to generate a perfect result in a single pass, these agentic patterns enable models to reason, utilize tools, critique their own outputs, and facilitate collaboration among specialized agents.

This repository demonstrates the following core design patterns:

1. **Reflection**
2. **Tool Use (Function Calling)** (integrated into the demos below)
3. **Reason and Act (ReAct)**
4. **Planning**
5. **Multi-Agent Collaboration**

## Getting Started

### Prerequisites

* **Python 3.11+**
* **Docker**
* **[Ollama](https://ollama.com/)** (Required for local LLM inference)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/shomec/agentic-ai-designpatterns.git
   cd agentic-ai-designpatterns
   ```

2. **Run the Demos:**

   To explore a pattern, navigate to its directory and use Docker Compose to build and run the application.

   * **Reflection Pattern**
     ```bash
     cd reflection
     docker compose up --build
     ```

   * **Reason and Act (ReAct) Pattern**
     ```bash
     cd reason-and-act
     docker compose up --build
     ```

   * **Planning Pattern**
     ```bash
     cd planning
     docker compose up --build
     ```

   * **Multi-Agent Collaboration Pattern**
     ```bash
     cd multi-agent
     docker compose up --build
     ```

   > **Note:** The **Tool Use** pattern is a fundamental capability demonstrated within the ReAct, Planning, and Multi-Agent demos.

## Tech Stack

This project leverages the following technologies to implement these patterns:

* **[Ollama](https://ollama.com/)**: Orchestrates local Large Language Models (specifically `gemma3:1b`).
* **[Model Context Protocol (MCP)](https://modelcontextprotocol.io/)**: Provides standardized, containerized access to external tools (e.g., DuckDuckGo Search) within the Docker environment.
* **Docker**: Ensures consistent and isolated execution environments for all services.
