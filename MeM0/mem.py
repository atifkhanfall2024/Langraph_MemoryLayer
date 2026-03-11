from mem0 import Memory
from dotenv import load_dotenv
import os
load_dotenv()
key = os.getenv("GOOGLE_API_KEY")
config={
    "version":"v1.1",
    "embedder":{
        "provider":"google-genai",
        "config":{"api_key":key , "model":"gemini-embedding-001" }
    } , 
    "llm":{
        "provider":"google-genai",
         "config":{"api_key":key , "model":"gemini-2.5-flash" }
    } ,
    "vector_store":{
        "provider":"qdrant",
        "config":{"host":"localhost" , "port":6333}
    }
}


memory = Memory.from_config(config)