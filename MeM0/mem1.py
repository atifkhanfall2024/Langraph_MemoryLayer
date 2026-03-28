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
            "port": 6333,
            "collection_name": "mem0"
        }
    }
}

# Initialize memory
memory = Memory.from_config(config)

# Take user input
while True:
 user_query = input(":> ")

 # also i need when user ask something then retireve this
 search = memory.search(query=user_query , user_id="atif")

 memories = [
   f" user id : {mem.get('id')}\n Memory : {mem.get('memory')}"
   for mem in search.get("results")
 ]

 print('memories ' , memories)

 system_prompt = f"""
You are an AI assistant.

Use the following user memories to answer the question:

{memories}

If the answer exists in memory, MUST use it.
If not, say you don't know.
"""

# Generate response using the Groq LLM inside Mem0
 ai_response = memory.llm.generate_response([
    {"role": "system", "content": system_prompt},
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