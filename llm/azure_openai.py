import os
import openai
from dotenv import load_dotenv

load_dotenv()

class AzureOpenAI:
    def __init__(self):
        self.api_key = os.getenv("AZURE_OPENAI_API_KEY")
        self.endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        openai.api_type = "azure"
        openai.api_key = self.api_key
        openai.api_base = self.endpoint

    def get_completion(self, prompt, **kwargs):
        # Example for GPT-35-Turbo deployment
        response = openai.ChatCompletion.create(
            engine="gpt-35-turbo",
            messages=[{"role": "user", "content": prompt}],
            **kwargs
        )
        return response["choices"][0]["message"]["content"]
