# import required libraries
import random

# define bot's responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hi! How can I assist you?"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day."],
    "default": ["I'm sorry, I didn't understand what you meant. Can you please rephrase?", 
                "I'm not sure what you mean. Could you please provide more context?"]
}

# define function to generate bot's response
def get_bot_response(user_message):
    if user_message in responses:
        return random.choice(responses[user_message])
    else:
        return random.choice(responses["default"])

# start chatting with the bot
while True:
    user_message = input("You: ")
    if user_message.lower() == "quit":
        break
    bot_response = get_bot_response(user_message.lower())
    print("Bot: " + bot_response)