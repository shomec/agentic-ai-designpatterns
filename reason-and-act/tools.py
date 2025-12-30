import asyncio
import os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

class Tool:
    def __init__(self, name, description, func):
        self.name = name
        self.description = description
        self.func = func

    def run(self, input_str):
        return self.func(input_str)

async def run_mcp_search(query):
    # Prepare the server parameters (docker command)
    server_params = StdioServerParameters(
        command="docker",
        args=["run", "-i", "--rm", "mcp/duckduckgo"],
        env=None
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            # Call the 'search' tool provided by mcp/duckduckgo
            result = await session.call_tool("search", arguments={"query": query})
            
            # Result is a CallToolResult
            text_content = []
            if result.content:
                for item in result.content:
                    if item.type == 'text':
                        text_content.append(item.text)
            
            return "\n".join(text_content)

def duckduckgo_search(query):
    """Searches the web using the mcp/duckduckgo MCP server."""
    try:
        return asyncio.run(run_mcp_search(query))
    except Exception as e:
        return f"MCP Search error: {e}"

def calculator(expression):
    """Evaluates a mathematical expression."""
    try:
        allowed = set("0123456789+-*/(). ")
        if not all(c in allowed for c in expression):
            return "Error: Invalid characters in expression."
        return str(eval(expression))
    except Exception as e:
        return f"Error evaluating expression: {e}"

# List of available tools
TOOLS = [
    Tool("Search", "Useful for when you need to answer questions about current events or people. Input should be a search query.", duckduckgo_search),
    Tool("Calculator", "Useful for performing mathematical calculations. Input should be a math expression.", calculator)
]
