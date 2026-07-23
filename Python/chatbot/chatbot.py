import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("Gemini AI Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Gemini Bot: Goodbye!")
        break

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=user_input
    )

    print("Gemini Bot:", response.text)