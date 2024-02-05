import random
import time
from datetime import date 

def greet_user():
    print("Hello! I'm your chatbot. How can I help you today?")

def farewell_message():
    print("Thank you for chatting with me. Have a great day!")

def chatbot_responses(user_response):
    if "hello" in user_response.lower() or "hi" in user_response.lower() or "hey" in user_response.lower():
        return "Hi there! How can I assist you?"
    elif "how are you" in user_response.lower() or "how you doing" in user_response.lower():
        return "I'm just a computer program, but how are you doing and yeah thanks for asking!"
    elif "i am fine" in user_response.lower() or "i'm doing good" in user_response.lower() or "i'm good" in user_response.lower():
        return "Wow, that's so nice to hear."
    elif "what's your name" in user_response.lower() or "what is your name" in user_response.lower() or "how are you called" in user_response.lower():
        return "I'm a chatbot, so I don't have a name. You can call me a Chatbot!"
    elif "what all tasks can you perform" in user_response.lower() or "can you help me with my homework" in user_response.lower():
        return "I'm still under development so I can't perform much tasks."
    elif "what is the time now" in user_response.lower() or "time" in user_response.lower():
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        return(current_time)
    elif "what is the date today" in user_response.lower() or "date" in user_response.lower():
        today = date.today()
        return today
    elif "bye" in user_response.lower() or "goodbye" in user_response.lower():
        farewell_message()
        return False
    else:
        return "I'm not sure how to respond to that. Can you ask me something else?"

def main():
    greet_user()
    while True:
        user_input = input("\nYour response: ")
        response = chatbot_responses(user_input)
        if response is not False:
            print(response)
        else: 
            break


if __name__ == "__main__":
    main()
