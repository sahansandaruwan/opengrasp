from src import geminiTextResponse

userInput = ""

while userInput != "exit":
    userInput = input("User : ")
    print(geminiTextResponse(userInput))



