import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.rag_pipeline import run_rag

st.set_page_config(page_title="RAG Chatbot", layout="wide")

st.title("🧠 Bedrock + Gemini Chatbot")

query = st.text_input("Ask a question:")

if st.button("Submit"):
    if query:
        with st.spinner("Thinking..."):
            answer, context = run_rag(query)

        st.subheader("💬 Answer")
        st.write(answer)

        with st.expander("📄 Show Context"):
            for i, chunk in enumerate(context):
                st.write(f"Chunk {i+1}:")
                st.write(chunk)
                st.write("---")