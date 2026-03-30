import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from mem0 import Memory
from dotenv import load_dotenv
import os
from qdrant_client import QdrantClient


load_dotenv()

GROQ_KEY = os.getenv("GROQ_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")  # Hugging Face token for embeddings

client = QdrantClient(host="localhost", port=6333)

client.recreate_collection(
    collection_name="mem0",
    vectors_config={
        "size": 384,
        "distance": "Cosine"
    }
)

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
  "graph_store": {
    "provider": "neo4j",
    "config": {
        "url": "neo4j+ssc://8f00d32f.databases.neo4j.io",
        "username": "neo4j",
        "password": "SOpvFH8dm-QqHltMFIQpoApy2icz4lFM8l0SDuzYj04",
        "database":"graph_store",
        "verify_ssl": False 
      
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
you pick the answer from memory if user ask and that present in memory 

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