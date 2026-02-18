from anthropic import Client
import os

# When using Anthropic’s API, you are not limited to just the user message.
# If you supply an assistant message, Claude will continue the conversation
# from the last assistant token.
# Just remember that we must start with a user message.

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

client = Client(api_key=anthropic_api_key)

messages = [
    {"role": "user", "content": f"Generate a beautiful haiku"},
    {"role": "assistant", "content": "calming mountain air"},
]

response = client.messages.create(
    model="claude-3-haiku-20240307", max_tokens=500, messages=messages
)

print(response.content[0].text)
