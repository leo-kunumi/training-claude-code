from anthropic import Client
import os

# "few-shot prompting" which involves providing a model with a small number of examples.
# We can provide Claude with a conversation history that shows exactly how we want it to respond.

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
client = Client(api_key=anthropic_api_key)

messages = [
    {
        "role": "user",
        "content": "Unpopular opinion: Pickles are disgusting. Don't @ me",
    },
    {"role": "assistant", "content": "NEGATIVE"},
    {
        "role": "user",
        "content": "I think my love for pickles might be getting out of hand. I just bought a pickle-shaped pool float",
    },
    {"role": "assistant", "content": "POSITIVE"},
    {
        "role": "user",
        "content": "Seriously why would anyone ever eat a pickle?  Those things are nasty!",
    },
    {"role": "assistant", "content": "NEGATIVE"},
    {
        "role": "user",
        "content": "Just tried the new spicy pickles from @PickleCo, and my taste buds are doing a happy dance! 🌶️🥒 #pickleslove #spicyfood",
    },
]

response = client.messages.create(
    model="claude-3-haiku-20240307", max_tokens=500, messages=messages
)

print(response.content[0].text)
