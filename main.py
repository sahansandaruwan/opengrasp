from google import genai
from dotenv import load_dotenv
import os
from src import geminiTextResponse


load_dotenv()

userInput = input("Type : ")
print(geminiTextResponse(userInput))





