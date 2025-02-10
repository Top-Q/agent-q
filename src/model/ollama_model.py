from dataclasses import dataclass
from ollama import Client
from smolagents import Model


@dataclass
class Message:
    content: str  # Required attribute for smolagents


class OllamaModel(Model):
    def __init__(self, model_name, host: str='localhost', ip: str='11434'):
        super().__init__()
        self.model_name = model_name
        self.client = Client(
            host=f'http://{host}:{ip}',
            headers={'x-some-header': 'some-value'}
        )

    def __call__(self, messages, **kwargs):
        formatted_messages = []

        # Ensure messages are correctly formatted
        for msg in messages:
            if isinstance(msg, str):
                formatted_messages.append({
                    "role": "user",  # Default to 'user' for plain strings
                    "content": msg
                })
            elif isinstance(msg, dict):
                role = msg.get("role", "user")
                content = msg.get("content", "")
                if isinstance(content, list):
                    content = " ".join(
                        part.get("text", "") for part in content if isinstance(part, dict) and "text" in part)
                formatted_messages.append({
                    "role": role if role in ['user', 'assistant', 'system', 'tool'] else 'user',
                    "content": content
                })
            else:
                formatted_messages.append({
                    "role": "user",  # Default role for unexpected types
                    "content": str(msg)
                })

        response = self.client.chat(
            model=self.model_name,
            messages=formatted_messages,
            options={'temperature': 0.7, 'stream': False}
        )

        # Return a Message object with the 'content' attribute
        return Message(
            content=response.get("message", {}).get("content", "")
        )
