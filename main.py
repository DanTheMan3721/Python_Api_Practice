import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("AIzaSyCE8y87en0Kgclk1MGn9CAl_z-XD69485o")

from google import genai

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.5-flash', contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
)
print(response.text)

def main():
    print("Hello from Build an AI agent in Python!")


if __name__ == "__main__":
    main()
