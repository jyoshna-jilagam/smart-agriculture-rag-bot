from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from knowledge_base import KNOWLEDGE_BASE

print("📚 Preparing knowledge documents...")

documents = []

for item in KNOWLEDGE_BASE:
    content = f"""
    {item['text']}

    Source: {item['source']}
    Reference: {item['url']}
    Topic: {item['topic']}
    """

    documents.append(
        Document(
            page_content=content,
            metadata={
                "topic": item["topic"],
                "source": item["source"]
            }
        )
    )

print("🧠 Generating embeddings...")

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("📦 Creating FAISS vector store...")

vectorstore = FAISS.from_documents(documents, embedding_model)

vectorstore.save_local("vector_store")

print("✅ Vector store created successfully!")
