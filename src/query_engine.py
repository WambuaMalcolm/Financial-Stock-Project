from llama_index.core import load_index_from_storage
from .index_news import create_or_load_index
from llama_index.core.prompts import PromptTemplate
index = create_or_load_index()

def create_query_engine():
    # Define the prompt template
    prompt_template = PromptTemplate(
        """\
    You are a helpful financial stock assistant that answers questions about news articles.
    You will be given a question and you should return the most relevant information from the indexed articles.

    Question: {query_str}

    Context: {context_str}

    Do not make up information, only use the indexed articles to answer the question.
    Do not answer questions that are not related to the indexed articles.

    Answer: """
    )

    # Create a query engine from the index
    
    return index.as_query_engine(
        text_qa_template = prompt_template
        # streaming = True,
        # verbose = True
    )

# Test the query engine with a sample question
query_engine = create_query_engine()
response = query_engine.query("Tell me about Google's new supercomputer.")
print("Answer:", response)
for node in response.source_nodes:
    print("\n--- Source ---")
    print("File:", node.node.metadata.get("file_name"))
    print("Snippet:", node.node.text[:300], "...")

if __name__ == "__main__":
    query_engine = create_query_engine()
    print("Query engine created successfully.")
