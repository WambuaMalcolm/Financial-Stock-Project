from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import os
from dotenv import load_dotenv
from pathlib import Path
import torch

def create_or_load_model():
    load_dotenv()
    # Set up Groq api key
    groq_api_key = os.getenv("GROQ_API_KEY")

    # Define cache directory
    CACHE_DIR = Path("cache/embeddings")
    CACHE_DIR.mkdir(parents=True, exist_ok=True)


    llm = Groq(
        api_key=groq_api_key,
        model="llama-3.3-70b-versatile",
        max_completion_tokens=256
    )
   
    # Initialize embeddings with cache directory
    embeddings = HuggingFaceEmbedding(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        cache_folder=str(CACHE_DIR),
    )
    #Memory cleanup
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    else:
        import gc
        gc.collect()
        torch.cuda.empty_cache()
        
    return llm, embeddings

        # # Clear CUDA cache if using GPU
        # if torch.cuda.is_available():
        #     torch.cuda.empty_cache()
        # else:
        #     # CPU memory cleanup
        #     import gc
        #     gc.collect()
        #     torch.cuda.empty_cache()

if __name__ == "__main__":
    llm, embeddings = create_or_load_model()
    print("LLM and embeddings initialized successfully.")