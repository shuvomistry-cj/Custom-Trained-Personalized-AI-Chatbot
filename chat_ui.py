import streamlit as st
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

# Streamlit UI Setup
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")
st.markdown("<h1 style='text-align: center;'>🤖 AI Chatbot</h1>", unsafe_allow_html=True)

# Session State for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to retrieve the most relevant chunk
def retrieve_answer(query, top_k=1):
    query_embedding = np.array([model.encode(query)])
    _, indices = index.search(query_embedding, top_k)
    return "\n".join([knowledge_base[i] for i in indices[0]])

# Display Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User Input
user_input = st.chat_input("Type your message...")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Retrieve context from FAISS
    context = retrieve_answer(user_input)

    # Generate AI response using Mistral API
    response = mistral.chat(
        model="mistral-tiny",
        messages=[
            {"role": "system", "content": "You are an assistant with knowledge from the user's website."},
            {"role": "user", "content": f"{user_input}\n\nContext:\n{context}"}
        ]
    )

    ai_response = response.choices[0].message.content.strip()

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(ai_response)

    # Append AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
