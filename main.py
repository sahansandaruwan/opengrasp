from src import geminiTextResponse

userInput = ""

while userInput == userInput:
    if userInput == "exit":
        break
    else:
        userInput = input("Type : ")
        print(geminiTextResponse(userInput))



