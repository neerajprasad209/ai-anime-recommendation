import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

MODEL_NAME = "llama-3.1-8b-instant"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

