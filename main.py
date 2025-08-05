from mcp_orchestrator import MCPOrchestrator

def main():
    orchestrator = MCPOrchestrator()
    print("Enter your prompt:")
    prompt = input()
    result = orchestrator.handle_prompt(prompt)
    print("Result:", result)

if __name__ == "__main__":
    main()
