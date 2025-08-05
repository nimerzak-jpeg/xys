# MCP Orchestrator Agent

This project is an orchestration agent for interacting with MCP servers (starting with GitHub MCP) using Azure OpenAI for prompt-driven automation.

## Structure

- `agents/` - MCP server-specific agent logic (start with GitHub)
- `llm/` - Azure OpenAI integration
- `scripts/` - Utilities for setup and running MCP servers
- `context_manager.py` - Context extraction from user prompts
- `mcp_orchestrator.py` - Main orchestration logic
- `main.py` - Entry point
- `.env` - Secrets/configuration
- `requirements.txt` - Python dependencies

## Setup

1. Copy `.env` and fill in your Azure OpenAI and GitHub credentials.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Use scripts in `scripts/` to clone and run the GitHub MCP server locally.
4. Run the orchestrator:
   ```sh
   python main.py
   ```

## Extending

- Add new agents in `agents/` for other MCP servers.
- Add new LLM providers in `llm/` as needed.
