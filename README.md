AI-Chatbot with FAISS & Mistral AI
Overview
This AI-powered chatbot retrieves knowledge using FAISS and generates responses using Mistral AI. It processes website content into a structured format, indexes it for efficient retrieval, and provides a web-based chat interface built with Streamlit.

![Image](https://github.com/user-attachments/assets/a5c9943c-74d3-446a-acfc-274dfef62d7f)

Features
✅ FAISS-based knowledge retrieval – Efficient vector-based search
✅ Mistral AI-powered response generation – Context-aware responses
✅ Data processing pipeline – Converts raw text into a structured knowledge base
✅ Interactive UI using Streamlit – User-friendly chat experience
✅ Stores chat history – Keeps track of interactions
✅ Easy deployment

Installation
1. Clone the Repository
git clone https://github.com/your-username/AI-Chatbot-FAISS-Mistral.git
cd AI-Chatbot-FAISS-Mistral

3. Install Dependencies
pip install streamlit faiss-cpu sentence-transformers mistralai beautifulsoup4

3. Prepare Data
Step 1: Extract Website Content
Use a web scraper (e.g., BeautifulSoup) to extract relevant text from a website.

Step 2: Preprocess the Data
Clean the extracted text (remove HTML tags, special characters, etc.).
Split the text into meaningful chunks.
Store the processed text in knowledge_base.json.
Step 3: Create FAISS Index
Encode the text chunks into embeddings using sentence-transformers.
Store the embeddings in faiss_index.bin for efficient retrieval.
Run the preprocessing script:

python data_processing.py
4. Run the Chatbot
streamlit run chat_ui.py

Project Structure

📂 AI-Chatbot-FAISS-Mistral
 ├── chatbot.py         # Core chatbot logic
 ├── chat_ui.py         # Streamlit UI
 ├── data_processing.py # Preprocesses website content
 ├── faiss_index.bin    # FAISS index file
 ├── knowledge_base.json # Knowledge base JSON
 ├── requirements.txt   # Python dependencies
 └── README.md          # Documentation

How It Works
Data Processing

Extracts and cleans website content.
Splits text into structured chunks.
Converts text into vector embeddings.
FAISS Indexing

Stores and retrieves relevant knowledge chunks.
Chatbot Response Generation

Retrieves relevant context from FAISS.
Uses Mistral AI to generate a response.
Streamlit UI

Provides an interactive chat interface.
Example Usage
Start the chatbot and enter a question.
The chatbot retrieves relevant context from FAISS.
Mistral AI generates a detailed response.
Future Improvements
Enhance multi-turn conversation memory
Improve UI with custom styles
Add voice input support
License
MIT License

