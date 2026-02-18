from anthropic import Anthropic
from dotenv import load_dotenv
import os

# https://github.com/anthropics/courses/blob/master/anthropic_api_fundamentals/01_getting_started.ipynb

load_dotenv()
my_api_key = os.getenv("ANTHROPIC_API_KEY")
if "=" in my_api_key:
    my_api_key = my_api_key.split("=")[1]

client = Anthropic(api_key=my_api_key)

our_first_message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "Hi there! Please write me a haiku about a pet chicken",
        }
    ],
)

print(our_first_message.content[0].text)
