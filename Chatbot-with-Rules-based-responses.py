
data = {
    "hi": "Hi there! I'm a friendly chatBot here to assist you?",
    "hello": "Hello! How can I help you today?",
    "what is your name": "I'm just a chatbot, so I don't have a name. You can call me Bhatbot.",
    "where are you from": "I'm from the digital world, always ready to chat !!",
    "how are you": "I'm just a ChatBot, but I'm here to assist you.",
    "do you have any hobbies or interests": "I'm always busy helping users, so my hobby is my work. I like to assist users.",
    "what did you eat today": "I don't eat, but I can help find delicious recipes and food-related information.",
    "do you enjoy listening music": "I can't listen to music, but I can suggest you some good music.",
    "bye": "Bye! Take care and have a great day!"
}

def get_response(user_input):
    user_input = user_input.lower()
    for pattern, response in data.items():
        if pattern in user_input:
            return response
    return "I'm sorry, I didn't understand that. Can you please rephrase your sentence?"

print("Chatbot: Hi! I'm a simple chatbot. I'm here to assist you!")

while True:
    user_input = input("Me: ")
    if user_input.lower() == 'bye':
        print("Chatbot:", data["bye"])
        break
    response = get_response(user_input)
    print("Chatbot:", response)
