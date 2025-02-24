import random as rd

dialogue_rules = {
    "Hello":["Hi friend, how are you?","Hello, how can I help you today?"],
    "I need some help with something":["Of course, I will help you with it. What can I do for you?","Don't worry about it, tell me what it is."],
    "Good bye":["Bye, have a nice day!. I'm always here if you need me!","Bye, take care"],
    "Thank you":["You are welcome. Do you need me to help with anything else?","Don't thank me, I'm here to help!"]
}

print("Welcome! Write me anything")
while True:
    question = input("You: ").strip()
    if question == "Out":
            print("Chatbot: Good bye!")
            break
    elif question not in dialogue_rules:
        print("Chatbot: Not in my language, write something else")
    else:
         print(f"Chatbot: {rd.choice(dialogue_rules[question])}")