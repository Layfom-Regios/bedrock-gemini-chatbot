🚀 Bedrock + Gemini RAG Chatbot

An end-to-end Retrieval-Augmented Generation (RAG) chatbot built using Amazon Bedrock Knowledge Base and Gemini 2.5 Flash.
This application retrieves relevant context from enterprise documents and generates accurate, context-aware responses.

🧠 Overview
This project combines:
Semantic search (RAG) using Amazon Bedrock Knowledge Base
LLM generation using Gemini 2.5 Flash
Interactive UI using Streamlit

👉 Result: Reliable answers grounded in your own data (reduced hallucination)

🔍 How It Works
User enters a query via Streamlit UI
Query is sent to Amazon Bedrock Knowledge Base
Relevant document chunks are retrieved
Gemini 2.5 Flash generates a response using retrieved context
Response + context is displayed to the user

🛠️ Tech Stack
Python
Streamlit
Amazon Bedrock Knowledge Base (RAG)
Gemini 2.5 Flash
Boto3
python-dotenv

✨ Features
✅ Context-aware responses
✅ Semantic search with vector retrieval
✅ Reduced hallucination
✅ Secure credential handling (IAM roles / .env)
✅ Interactive UI
✅ Deployable on AWS EC2


📁 Project Structure
bedrock-gemini-chatbot/
│
├── app/
│   └── main.py                # Streamlit UI
│
├── backend/
│   ├── backend.py            # Bedrock retrieval logic
│   └── rag_pipeline.py       # RAG pipeline orchestration
│
├── .env                      # Environment variables
├── requirements.txt          # Dependencies
└── README.md

⚙️ Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/bedrock-gemini-chatbot.git
cd bedrock-gemini-chatbot

2️⃣ Install Dependencies
pip3 install -r requirements.txt

3️⃣ Configure Environment Variables
Create a .env file:
AWS_REGION=us-east-1
KNOWLEDGE_BASE_ID=your_kb_id
GEMINI_API_KEY=your_api_key

4️⃣ Run Application
streamlit run app/main.py

🌐 Deployment (AWS EC2)
Launch EC2 instance (Amazon Linux)
Attach IAM role with:
AmazonBedrockFullAccess
Open port 8501 in security group

Run app:
nohup streamlit run app/main.py --server.port 8501 --server.address 0.0.0.0 &
🔗 Access App
http://<EC2_PUBLIC_IP>:8501

💡 Key Learnings
Implementing RAG using Amazon Bedrock
Integrating external LLMs (Gemini)
Managing IAM roles securely
Deploying scalable GenAI apps on AWS
