from src import geminiTextResponse

userInput = ""

while userInput != "exit":
    userInput = input("Type : ")
    print(geminiTextResponse(userInput))



