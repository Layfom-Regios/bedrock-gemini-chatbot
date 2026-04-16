from backend.backend import retrieve_context
from backend.gemini import generate_answer

def run_rag(query):
    chunks = retrieve_context(query)

    context = "\n\n".join(chunks)

    answer = generate_answer(context, query)

    return answer, chunks