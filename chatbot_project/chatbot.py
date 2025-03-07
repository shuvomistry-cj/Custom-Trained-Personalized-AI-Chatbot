import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from mistralai.client import MistralClient

# Load FAISS index and knowledge base
index = faiss.read_index("faiss_index.bin")
with open("knowledge_base.json", "r", encoding="utf-8") as file:
    knowledge_base = json.load(file)

# Load Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize Mistral AI client
mistral = MistralClient(api_key="9v9MHOuPAHv0jXTaN9IUjkVrl6AGiC7p")

def retrieve_answer(query, top_k=1):
    """Retrieve the most relevant chunk from FAISS index."""
    query_embedding = np.array([model.encode(query)])
    _, indices = index.search(query_embedding, top_k)
    return "\n".join([knowledge_base[i] for i in indices[0]])

def chat():
    """Simple chatbot loop."""
    print("\n🤖 Chatbot is ready! Type 'exit' to stop.")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            print("👋 Goodbye!")
            break
        context = retrieve_answer(query)
        response = mistral.chat(model="mistral-tiny", messages=[
            {"role": "system", "content": "You are an assistant with knowledge from the user's website."},
            {"role": "user", "content": f"{query}\n\nContext:\n{context}"}
        ])
        print("🤖:", response.choices[0].message.content.strip())


if __name__ == "__main__":
    chat()
