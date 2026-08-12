from google import genai
from dotenv import load_dotenv
import os

load_dotenv()



geminiApiKey = os.getenv('GEMINI_API_KEY')
client = genai.Client(api_key=geminiApiKey)

def geminiTextResponse(userInput):
    interaction = client.interactions.create(model="gemini-3.6-flash", input=userInput)
    return interaction.output_text
