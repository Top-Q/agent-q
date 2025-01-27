import requests
from smolagents import CodeAgent, OpenAIServerModel

# class OpenAIServerModel(Model):
#     def __init__(self, api_url):
#         self.api_url = api_url
#
#     def chat(self, messages):
#         payload = {"model": "Qwen/Qwen2.5-Coder-3B-Instruct-GGUF", "messages": messages}
#         response = requests.post(self.api_url, json=payload)
#         return response.json()["choices"][0]["message"]["content"]
#
# Replace with your API Gateway URL

model = OpenAIServerModel(api_base="http://127.0.0.1:1234/v1", model_id="Qwen/Qwen2.5-Coder-3B-Instruct-GGUF", api_key="")
agent = CodeAgent(model=model, tools=[])
print(agent.run("Tell me about SmolAgents."))