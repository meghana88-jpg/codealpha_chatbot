
def chatbot_response(user_input):
    message = user_input.lower().strip()

    if message == "hello" or message == "hi":
        return "Hi! How can I help you?"

    elif message == "how are you":
        return "I'm fine, thanks!"

    elif message == "what is your name":
        return "I'm a simple Python chatbot."

    elif message == "help":
        return "You can say hello, ask how I am, or ask my name."

    elif message == "bye" or message == "goodbye":
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I don't understand that message."


def main():
    print("Welcome to the Basic Chatbot!")
    print("Type 'bye' to exit the chatbot.")
    print("----------------------------------")

    while True:
        user_input = input("You: ")

        response = chatbot_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() in ["bye", "goodbye"]:
            break


if __name__ == "__main__":
    main()
