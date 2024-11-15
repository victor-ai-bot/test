import random

# Define a set of responses
responses = {
    "hello": ["Hi!", "Hello!", "Greetings!"],
    "how are you": ["I'm doing well, thank you!", "I'm great, how about you?",
                    "I'm just a chatbot, but I'm doing fine!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "default": ["Sorry, I didn't understand that.", "Can you rephrase?", "I'm not sure what you mean."]
}


def get_response(user_input):
    # Convert the input to lowercase for easier matching
    user_input = user_input.lower()

    # Check if the input matches any predefined responses
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    # If no match, return a default response
    return random.choice(responses["default"])


def chatbot():
    print("Hello! I'm your friendly chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break

        response = get_response(user_input)
        print("Chatbot:", response)


# Run the chatbot
chatbot()
