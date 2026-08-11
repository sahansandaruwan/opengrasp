from google import genai
from dotenv import load_dotenv
import os


load_dotenv()

geminiApiKey = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=geminiApiKey)

interaction = client.interactions.create(model="gemini-3.6-flash", input="How are You")

print(interaction.output_text)
