from anthropic import Client
import os

# https://github.com/anthropics/courses/blob/master/anthropic_api_fundamentals/02_messages_format.ipynb


def translate(word: str, language: str) -> str:
    anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
    client = Client(api_key=anthropic_api_key)
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        messages=[{"role": "user", "content": f"Translate {word} to {language}."}],
    )
    print(response.content[0].text)


translate("hello", "Spanish")
translate("chicken", "Italian")
