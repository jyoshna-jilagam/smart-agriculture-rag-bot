import os
import streamlit as st
import requests

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document


# -------------------------
# 🔐 Load API Key (Streamlit Cloud)
# -------------------------
OPENROUTER_API_KEY = st.secrets.get("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    st.error("❌ OPENROUTER_API_KEY not found in Streamlit Secrets.")
    st.stop()


# -------------------------
# 🎨 Page Config
# -------------------------
st.set_page_config(
    page_title="🌾 Smart Agriculture RAG Bot",
    layout="wide"
)

st.title("🌾 Smart Agriculture Crop Process Explainer Bot")
st.markdown("AI-powered educational assistant for crop lifecycle and farming processes.")


# -------------------------
# 📦 Load or Create Vector Store
# -------------------------
@st.cache_resource
def load_vector_store():
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # If vector store exists → load it
    if os.path.exists("vector_store/index.faiss"):
        return FAISS.load_local(
            "vector_store",
            embedding_model,
            allow_dangerous_deserialization=True
        )

    # Otherwise → create a basic one automatically
    st.warning("⚠️ Vector store not found. Creating default knowledge base...")

    documents = [
        Document(page_content="Crop lifecycle includes soil preparation, sowing, irrigation, fertilization, and harvesting."),
        Document(page_content="Proper irrigation is essential for maintaining soil moisture."),
        Document(page_content="Weed management helps improve crop productivity."),
        Document(page_content="Harvesting should be done at the right maturity stage."),
    ]

    vectorstore = FAISS.from_documents(documents, embedding_model)
    vectorstore.save_local("vector_store")

    return vectorstore


try:
    vectorstore = load_vector_store()
except Exception as e:
    st.error(f"⚠️ Failed to load vector store: {str(e)}")
    st.stop()


# -------------------------
# 🚨 Safety Filter
# -------------------------
def is_restricted(query):
    restricted_terms = [
        "fertilizer",
        "chemical dosage",
        "pesticide amount",
        "yield prediction",
        "how much urea",
        "profit estimate"
    ]
    return any(term in query.lower() for term in restricted_terms)


# -------------------------
# 🤖 OpenRouter LLM Function
# -------------------------
def generate_answer(query, context):

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
You are an agriculture education assistant.

Only provide informational explanations.
Do NOT provide fertilizer advice, chemical dosage, or yield prediction.

Context:
{context}

Question:
{query}

Provide a simple explanation suitable for farmers.
"""

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )

        if response.status_code != 200:
            return f"⚠️ API Error ({response.status_code}): {response.text}"

        result = response.json()

        if "choices" not in result or not result["choices"]:
            return f"⚠️ Unexpected API response: {result}"

        return result["choices"][0]["message"]["content"]

    except requests.exceptions.Timeout:
        return "⚠️ Request timed out. Please try again."

    except Exception as e:
        return f"⚠️ System Error: {str(e)}"


# -------------------------
# 🔍 Query Interface
# -------------------------
user_query = st.text_input("Ask your agriculture-related question:")

if user_query:

    if is_restricted(user_query):
        st.warning("⚠️ This system provides educational explanations only.")
    else:
        with st.spinner("🔎 Searching knowledge base..."):
            docs = vectorstore.similarity_search(user_query, k=3)
            context = "\n\n".join([doc.page_content for doc in docs])

        with st.spinner("🤖 Generating response..."):
            answer = generate_answer(user_query, context)

        st.success("✅ Answer")
        st.write(answer)

        st.markdown("### 📖 Sources")
        for doc in docs:
            st.write(f"- {doc.metadata.get('source', 'Knowledge Base')}")
