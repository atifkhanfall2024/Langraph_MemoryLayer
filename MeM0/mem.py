from mem0 import Memory
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

key = os.getenv("GROQ_API_KEY")

config = {
    "version": "v1.1",
    "embedder": {
        "provider": "groq",
        "config": {"api_key": key, "model": "mixtral-8x7b-32768"}
    },
    "llm": {
        "provider": "groq",
        "config": {"api_key": key, "model": "mixtral-8x7b-32768"}
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {"host": "localhost", "port": 6333}
    }

}



# Initialize memory
memory = Memory.from_config(config)

# Take user input
user_query = input(":> ")

# Gemini client using OpenAI-compatible API
client = OpenAI(
    api_key=key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "user", "content": user_query}
    ]
)

ai_response = response.choices[0].message.content

print("AI Response:", ai_response)

# Store conversation in memory
memory.add(
    user_id="atif",
    messages=[
        {"role": "user", "content": user_query},
        {"role": "assistant", "content": ai_response}
    ]
)

print("Data stored into DB")