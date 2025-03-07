import os
import re
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# File Paths
EXTRACTED_TEXT_FILE = "extracted_all_pages.txt"
PROCESSED_TEXT_FILE = "processed_knowledge.txt"
KNOWLEDGE_JSON_FILE = "knowledge_base.json"
FAISS_INDEX_FILE = "faiss_index.bin"

# Load extracted data
if not os.path.exists(EXTRACTED_TEXT_FILE):
    raise FileNotFoundError(f"❌ File '{EXTRACTED_TEXT_FILE}' not found!")

with open(EXTRACTED_TEXT_FILE, "r", encoding="utf-8") as file:
    raw_text = file.read().strip()

if not raw_text:
    raise ValueError("❌ Extracted text file is empty!")

print(f"✅ Loaded extracted text ({len(raw_text)} characters)")

# Split text into chunks
def split_text(text, chunk_size=500):
    sentences = re.split(r'(?<=[.!?])\s+', text)  # Split by sentence
    chunks, current_chunk = [], ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) < chunk_size:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
    
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

chunks = split_text(raw_text)

if not chunks:
    raise ValueError("❌ No chunks generated!")

print(f"✅ Split into {len(chunks)} chunks")

# Save processed text to file
with open(PROCESSED_TEXT_FILE, "w", encoding="utf-8") as file:
    file.write("\n".join(chunks))

print(f"✅ Processed text saved to '{PROCESSED_TEXT_FILE}'")

# Load sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")
print("✅ Sentence Transformer model loaded")

# Convert text chunks to vector embeddings
embeddings = np.array([model.encode(chunk) for chunk in chunks])

# Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Save FAISS index
faiss.write_index(index, FAISS_INDEX_FILE)
print(f"✅ FAISS index saved to '{FAISS_INDEX_FILE}'")

# Save knowledge base as JSON
with open(KNOWLEDGE_JSON_FILE, "w", encoding="utf-8") as file:
    json.dump(chunks, file, indent=4)

print(f"✅ Knowledge base saved to '{KNOWLEDGE_JSON_FILE}'")

print("🎉 Data processing complete!")
