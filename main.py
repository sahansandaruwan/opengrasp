from src import geminiTextResponse

userInput = ""

<<<<<<< HEAD
while userInput == userInput:
    if userInput == "exit":
        break
    else:
        userInput = input("Type : ")
        print(geminiTextResponse(userInput))
=======
while userInput != "exit":
    userInput = input("User : ")
    print(geminiTextResponse(userInput))
>>>>>>> ff6728b42e75ec7c9de3b6d33df69ce3c62e0e7b



