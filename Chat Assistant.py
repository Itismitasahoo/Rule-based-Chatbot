#Rule based AI Python Chatbot

import datetime
import time
name = input("Welcome!! Enter your name : ")
presentHour = datetime.datetime.now().hour

if 5<= presentHour<=11 :
    print("Good Morning ," ,name)
elif 11< presentHour<=17 :
    print("Good afternoon," ,name )
elif 17<presentHour<=20 :
    print("Good evening, " ,name)
else:
    print("Good night," , name)


print("Hello! Welcome to ChatBot")
print("You can ask me basic questions , Type 'bye' to exit from the bot. ")

#chatbot Memory Creation [dictionary of responses]

responses ={
    "hello" :"Hii, How can I assist you ?" ,
    "how are you " :"I am fine. Thank you" ,
    "Who are you ?" :"I am smart AI Chatbot.",
    "Motivate me" :"Keep going. Every bug of your code makes you a better developer.",
    "happy" :"Graet to hear that.",
    "thank you" :"You are most welcome."
}

#Function to get response of chatbot
def getResponseOfBot(userQuestion) :
    useQuestion = userQuestion.lower().strip()
    for key in  responses.keys():
        if key in userQuestion :
            return responses[key]
    
    return "I am not able to tell this. I will try to answer soon."
#Take user input
while True :
    userInput = input("Please ask your question : ")
    reply = getResponseOfBot(userInput)
    print("Bot response: ",reply)

    if "bye" in userInput.lower():
        break