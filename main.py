
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("🤖 AI Assistant is ready!")
while True:
    user_input = input("Ask me anything (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",

        messages=[
            {"role": "system", "content": "You are a helpful AI assistant that explains concepts clearly."},
            {"role": "user", "content": user_input}
        ]
    )

    print("\nAI Assistant:", response.choices[0].message.content)
    print("-" * 50)
