import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# Load knowledge base
with open("processed_knowledge.txt", "r", encoding="utf-8") as f:
    knowledge_data = [line.strip() for line in f.readlines() if line.strip()]  # Remove empty lines

if not knowledge_data:
    print("❌ Error: Knowledge base is empty. Please check 'processed_knowledge.txt'.")
    exit()

# Initialize embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")  # Small and efficient

# Convert text to embeddings
embeddings = model.encode(knowledge_data, convert_to_numpy=True)

# Check if embeddings were generated
if embeddings.shape[0] == 0:
    print("❌ Error: Embeddings are empty. Please check your text data.")
    exit()

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save FAISS index
faiss.write_index(index, "knowledge_index.faiss")

# Save text mappings
with open("knowledge_texts.json", "w", encoding="utf-8") as f:
    json.dump(knowledge_data, f)

print("✅ Knowledge base embedded and saved as 'knowledge_index.faiss'")
