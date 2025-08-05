import os
import requests
from dotenv import load_dotenv

load_dotenv()

class GitHubMCPAgent:
    def __init__(self):
        self.mcp_url = os.getenv("MCP_SERVER_URL")
        self.github_token = os.getenv("GITHUB_TOKEN")

    def provision(self, payload):
        headers = {"Authorization": f"Bearer {self.github_token}"}
        response = requests.post(f"{self.mcp_url}/provision", json=payload, headers=headers)
        response.raise_for_status()
        return response.json()

    # Add more methods for other MCP actions as needed
