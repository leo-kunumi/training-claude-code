from anthropic import Client
import os

# Keep a list to store the conversation history
# Ask a user for a message using input() and add the user input to the messages list
# Send the message history to Claude
# Print out Claude's response to the user
# Add Claude's assistant response to the history
# Go back to step 2 and repeat! (use a loop and provide a way for users to quit!)

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
client = Client(api_key=anthropic_api_key)

conversation_history = []

while True:
    user_input = input("User: ")

    if user_input.lower() == "quit":
        print("Conversation ended.")
        break

    conversation_history.append({"role": "user", "content": user_input})

    response = client.messages.create(
        model="claude-3-haiku-20240307", messages=conversation_history, max_tokens=500
    )

    assistant_response = response.content[0].text
    print(f"Assistant: {assistant_response}")
    conversation_history.append({"role": "assistant", "content": assistant_response})
