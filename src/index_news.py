from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

from llama_index.core import Settings

from llama_index.core.node_parser import SentenceSplitter

from pathlib import Path

from .models import create_or_load_model

llm, embeddings = create_or_load_model()


INDEX_DIR = Path("articles_index")

def create_or_load_index():
    Settings.llm = llm
    Settings.embed_model = embeddings
    Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=30)
    Settings.num_output = 512
    Settings.context_window = 2048

    if INDEX_DIR.exists():
        print("Loading existing index...")
        storage_context = StorageContext.from_defaults(persist_dir = INDEX_DIR)
        return load_index_from_storage(storage_context)
    
    else:
        print("Creating new index...")
        documents = SimpleDirectoryReader("articles").load_data()
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=INDEX_DIR)
        return index
if __name__ == "__main__":
    index = create_or_load_index()