from mem0 import Memory
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_KEY = os.getenv("GROQ_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")  # Hugging Face token for embeddings

config = {
    "version": "v1.1",
    "embedder": {
        "provider": "huggingface",
        "config": {
            "model": "sentence-transformers/all-MiniLM-L6-v2",
            "api_key": HF_TOKEN
        }
    },
    "llm": {
        "provider": "groq",
        "config": {
         "model": "llama-3.3-70b-versatile",  # <-- updated model
        "api_key": GROQ_KEY,
        "temperature": 0.1,
        "max_tokens": 1000
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333
        }
    }
}

# Initialize memory
memory = Memory.from_config(config)

# Take user input
user_query = input(":> ")

# Generate response using the Groq LLM inside Mem0
ai_response = memory.llm.generate_response([
    {"role": "user", "content": user_query}
])

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