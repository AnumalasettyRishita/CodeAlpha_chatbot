#chatbot by codealpha
def chatbot():
     print("welcome to simple chatbot!")
     print("Type 'bye' to exit")
     while True:
        user = input("You:").lower()
        if user == "hello":
           print("Bot: Hi! Nice to meet you.")
        elif user == "how are you":
           print("Bot: I am fine.How are you?")
        elif user == "what is your name":
           print("Bot: My name is CodeAlpha Bot.")
        elif user == "good":
           print("Bot: That's great to here!")
        elif user == "bye":
           print("Bot: Goodbye! Have a nice day.")
           break
        else:
           print("Bot: Sorry,I don't understand that.")
chatbot()
 