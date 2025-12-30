# Agentic AI Design Patterns

Welcome to my Agentic AI Design Patterns repository. I created this project to showcase the various "Agentic AI" design patterns, that has been popularized by [DeepLearning.AI](https://www.deeplearning.ai/), with real working demo apps or code examples on how to build autonomous, iterative, and collaborative agentic AI apps. I took help of **Google Anti Gravity** to generate some of these codes.

This repo demonstrates the following core agentic AI design patterns:

1. **Reflection**
2. **Tool Use (Function Calling)**
3. **Planning**
4. **Multi-Agent Collaboration**

## Getting Started

### Prerequisites

* Python 3.11+
* Docker
* [Ollama LLM](https://ollama.com/)

### Installation

#### Clone the repo:

```bash
git clone https://github.com/shomec/agentic-ai-designpatterns.git
cd agentic-ai-designpatterns
```

#### Setup environment:

To run working demos of individual design patterns, cd into the corresponding directory and run docker compose to build and run the services:

* For **"reflection pattern"** demo:
  ```bash
  cd reflection
  docker compose up --build
  ```

* For **"reason-and-act (ReAct) pattern"** demo:
  ```bash
  cd reason-and-act
  docker compose up --build
  ```

* For **"planning pattern"** demo:
  ```bash
  cd planning
  docker compose up --build
  ```

* For **"multi-agent orchestration or collaboration pattern"** demo:
  ```bash
  cd multi-agent
  docker compose up --build
  ```


### Tech Stack

This repository utilizes the following frameworks and tools to implement these patterns:

* **Ollama**: For running local LLMs (Llama 3.2).
* **MCP Server** (DuckDuckGo): For providing real-time search capabilities via Docker.

