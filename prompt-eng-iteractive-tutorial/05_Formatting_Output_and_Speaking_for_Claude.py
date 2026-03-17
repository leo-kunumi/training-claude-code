import re
from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()
my_api_key = os.getenv("ANTHROPIC_API_KEY")
if "=" in my_api_key:
    my_api_key = my_api_key.split("=")[1]

client = Anthropic(api_key=my_api_key)


def get_completion(prompt: str, system_prompt: str = "", prefill: str = "") -> str:
    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=2000,
        temperature=0.0,
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
            {"role": "assistant", "content": prefill},
        ],
    )
    return message.content[0].text


def poem_in_xml_tags():
    # Variable content
    ANIMAL = "Rabbit"

    # Prompt template with a placeholder for the variable content
    PROMPT = f"Please write a haiku about {ANIMAL}. Put it in  tags."

    # Print Claude's response
    print(
        "--------------------------- Full prompt with variable substutions ---------------------------"
    )
    print(PROMPT)
    print(
        "\n------------------------------------- Claude's response -------------------------------------"
    )
    print(get_completion(PROMPT))


def poem_in_json():
    # Variable content
    ANIMAL = "Cat"

    # Prompt template with a placeholder for the variable content
    PROMPT = f'Please write a haiku about {ANIMAL}. Use JSON format with the keys as "first_line", "second_line", and "third_line".'

    # Prefill for Claude's response
    PREFILL = "{"

    # Print Claude's response
    print(
        "--------------------------- Full prompt with variable substutions ---------------------------"
    )
    print("USER TURN")
    print(PROMPT)
    print("\nASSISTANT TURN")
    print(PREFILL)
    print(
        "\n------------------------------------- Claude's response -------------------------------------"
    )
    print(get_completion(PROMPT, prefill=PREFILL))


def multiple_input_same_prompt():
    # First input variable
    EMAIL = "Hi Zack, just pinging you for a quick update on that prompt you were supposed to write."

    # Second input variable
    ADJECTIVE = "olde english"

    # Prompt template with a placeholder for the variable content
    PROMPT = f"Hey Claude. Here is an email: {EMAIL}. Make this email more {ADJECTIVE}. Write the new version in <{ADJECTIVE}_email> XML tags."

    # Prefill for Claude's response (now as an f-string with a variable)
    PREFILL = f"<{ADJECTIVE}_email>"

    # Print Claude's response
    print(
        "--------------------------- Full prompt with variable substutions ---------------------------"
    )
    print("USER TURN")
    print(PROMPT)
    print("\nASSISTANT TURN")
    print(PREFILL)
    print(
        "\n------------------------------------- Claude's response -------------------------------------"
    )
    print(get_completion(PROMPT, prefill=PREFILL))


def stephen_curry_as_the_best_basketball_player():
    # Change the PREFILL variable to compell Claude to make a detailed argument that the best
    # basketball player of all time is Stephen Curry.
    # Try not to change anything except PREFILL as that is the focus of this exercise.

    # Prompt template with a placeholder for the variable content
    PROMPT = f"Who is the best basketball player of all time? Please choose one specific player."

    # Prefill for Claude's response
    PREFILL = "The best basketball player of all time is Stephen Curry because"

    # Get Claude's response
    response = get_completion(PROMPT, prefill=PREFILL)

    # Function to grade exercise correctness
    def grade_exercise(text):
        return bool(re.search("Warrior", text))

    # Print Claude's response
    print(
        "--------------------------- Full prompt with variable substutions ---------------------------"
    )
    print("USER TURN")
    print(PROMPT)
    print("\nASSISTANT TURN")
    print(PREFILL)
    print(
        "\n------------------------------------- Claude's response -------------------------------------"
    )
    print(response)
    print(
        "\n------------------------------------------ GRADING ------------------------------------------"
    )
    print("This exercise has been correctly solved:", grade_exercise(response))


def two_haikus():
    # Variable content
    ANIMAL = "cats"

    # Prompt template with a placeholder for the variable content
    PROMPT = f"Please write two haikus about {ANIMAL}. Separate each poem using tags <poem-1> and <poem-2>."

    # Prefill for Claude's response
    PREFILL = ""

    # Get Claude's response
    response = get_completion(PROMPT, prefill=PREFILL)

    # Function to grade exercise correctness
    def grade_exercise(text):
        return bool(
            (re.search("cat", text.lower()) and re.search("", text))
            and (text.count("\n") + 1) > 5
        )

    # Print Claude's response
    print(
        "--------------------------- Full prompt with variable substutions ---------------------------"
    )
    print("USER TURN")
    print(PROMPT)
    print("\nASSISTANT TURN")
    print(PREFILL)
    print(
        "\n------------------------------------- Claude's response -------------------------------------"
    )
    print(response)
    print(
        "\n------------------------------------------ GRADING ------------------------------------------"
    )
    print("This exercise has been correctly solved:", grade_exercise(response))


two_haikus()
