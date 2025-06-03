def chatbot():
    print("Hello! I'm ChatBot. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ['hi', 'hello', 'hey']:
            print("Bot: Hello! How can I help you today?")

        elif 'your name' in user_input:
            print("Bot: I'm a simple chatbot built with Python!")

        elif 'how are you' in user_input:
            print("Bot: I'm just a bunch of code, but I'm doing great!")

        elif 'help' in user_input:
            print("Bot: I can respond to greetings, tell you my name, and answer simple questions.")

        elif 'bye' in user_input or user_input == 'exit':
            print("Bot: Goodbye! Have a great day!")
            break

        elif 'weather' in user_input:
            print("Bot: I'm not connected to the internet, so I can't check the weather right now.")

        elif 'joke' in user_input:
            print("Bot: Why don’t scientists trust atoms? Because they make up everything!")

        else:
            print("Bot: I'm not sure how to respond to that. Try asking something else.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()

