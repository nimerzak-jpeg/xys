from context_manager import ContextManager
from llm.azure_openai import AzureOpenAI
from agents.github_agent import GitHubMCPAgent

class MCPOrchestrator:
    def __init__(self):
        self.context_manager = ContextManager()
        self.llm = AzureOpenAI()
        self.github_agent = GitHubMCPAgent()

    def handle_prompt(self, prompt: str):
        context = self.context_manager.extract_context(prompt)
        llm_response = self.llm.get_completion(prompt)
        # For now, assume LLM response is a JSON payload for provisioning
        # In production, parse/validate LLM output
        try:
            import json
            payload = json.loads(llm_response)
        except Exception:
            payload = {"llm_response": llm_response}
        result = self.github_agent.provision(payload)
        return result
