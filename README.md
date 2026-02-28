# 🌾 Smart Agriculture Crop Process Explainer Bot

> 🚜 Responsible AI-powered RAG system for Agricultural Education  
> 🔐 Safe • Domain-Restricted • Retrieval-Grounded • Hackathon Ready  

---

## 📌 Overview

The **Smart Agriculture Crop Process Explainer Bot** is a Retrieval-Augmented Generation (RAG) based chatbot designed to explain crop lifecycle stages and farming processes in simple, easy-to-understand language.

This system strictly avoids:
- ❌ Fertilizer recommendations  
- ❌ Pesticide advice  
- ❌ Treatment guidance  
- ❌ Yield prediction  

It demonstrates **ethical and responsible AI deployment in agriculture**.

---

# 🎯 Problem Statement

- Agricultural documentation is often technical and complex.
- Farmers may lack structured understanding of crop lifecycle stages.
- Extension officers repeatedly explain the same processes.
- Generative AI systems may provide unsafe advisory content.

There is a need for a **safe, educational AI system** focused only on awareness.

---

# 💡 Our Solution

We built a **domain-controlled RAG chatbot** that:

✔ Retrieves verified crop lifecycle knowledge  
✔ Generates simplified explanations using Gemini Flash  
✔ Applies strict safety filtering  
✔ Prevents harmful agricultural advisory outputs  

---

# 🧠 System Architecture

## 🔷 High-Level Architecture

```
User Query
   ↓
Streamlit Interface
   ↓
Safety & Intent Filter
   ↓
Query Embedding
   ↓
FAISS Vector Search
   ↓
Top-K Context Retrieval
   ↓
Prompt Construction
   ↓
Gemini Flash (LLM)
   ↓
Safe Informational Response
```

---

## 🔷 Detailed RAG Pipeline

### 1️⃣ Knowledge Base Layer
- Agricultural lifecycle PDF
- Clean, domain-restricted content
- No advisory data included

### 2️⃣ Text Chunking
- Split into small overlapping chunks
- Improves retrieval accuracy
- Reduces hallucination

### 3️⃣ Embedding Layer
- SentenceTransformer (`all-MiniLM-L6-v2`)
- Converts text into numerical vectors

### 4️⃣ Vector Database
- FAISS IndexFlatL2
- Fast similarity search
- Lightweight and hackathon friendly

### 5️⃣ Retrieval Layer
- Query converted to embedding
- Top-K relevant chunks retrieved
- Context injected into prompt

### 6️⃣ Controlled Generation Layer
- Gemini Flash model via Google AI Studio
- Strong system instructions
- Domain-restricted output

### 7️⃣ Output Guard Layer
- Keyword-based restriction
- Blocks fertilizer & yield queries
- Ensures safe AI usage

---

# 🛠️ Tech Stack

| Layer | Technology |
|--------|------------|
| Frontend | Streamlit |
| Backend | Python |
| LLM | Gemini Flash |
| API Platform | Google AI Studio |
| Embeddings | Sentence Transformers |
| Vector DB | FAISS |
| Document Parsing | PyPDF |
| Chunking | LangChain |

---

# 🔄 End-to-End Usage Flow

## Step 1: User Interaction
User enters:
```
Explain irrigation cycle
```

## Step 2: Safety Filtering
System checks for restricted intent.

If restricted:
```
⚠️ I can only explain crop lifecycle and farming processes.
```

## Step 3: Query Embedding
Query converted into vector representation.

## Step 4: Similarity Search
FAISS retrieves relevant agricultural chunks.

## Step 5: Prompt Construction
Final prompt includes:
- System safety instruction
- Retrieved context
- User question

## Step 6: LLM Generation
Gemini Flash generates:
- Structured
- Simple
- Informational explanation

## Step 7: Display Output
Streamlit presents formatted answer.

---

# 🔐 Responsible AI Measures

This project includes multiple safety layers:

### ✅ Query Filtering
Blocks advisory-related keywords.

### ✅ Domain Restriction
Knowledge base excludes treatment & fertilizer content.

### ✅ Prompt Guardrails
Strict system-level instructions.

### ✅ No Predictive Models
No yield forecasting or optimization algorithms.

---

# 📂 Project Structure

```
smart-agriculture-rag-bot/
│
├── app.py
├── create_vector_store.py
├── requirements.txt
├── README.md
├── vector_store.index
├── chunks.pkl
│
├── data/
│   └── agriculture_docs.pdf
│
├── assets/
│   └── architecture.png
│
└── docs/
    └── project_report.pdf
```

---

# 🚀 How to Run

## 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2️⃣ Set API Key

**Mac / Linux**
```bash
export GOOGLE_API_KEY="your_key"
```

**Windows**
```bash
set GOOGLE_API_KEY=your_key
```

---

## 3️⃣ Create Vector Store

```bash
python create_vector_store.py
```

This generates:
- `vector_store.index`
- `chunks.pkl`

---

## 4️⃣ Run the Application

```bash
streamlit run app.py
```

---

# 🌍 Impact

- Improves agricultural awareness
- Reduces misinformation
- Demonstrates safe GenAI deployment
- Assists rural knowledge dissemination
- Scalable for multilingual support

---

# 🔮 Future Enhancements

- 🌐 Multilingual support (Hindi, Telugu)
- 🎤 Voice-based assistant
- 📱 SMS-based rural deployment
- 📚 Crop-specific knowledge modules
- 🏛 Government agriculture portal integration

---

# 🏆 Why This Project Stands Out

✔ Responsible AI Architecture  
✔ Domain-Specific RAG Implementation  
✔ Safety-First Design  
✔ Real-World Agricultural Impact  
✔ Clean, Deployable System  

---

# 📜 License

For educational and research purposes.

---

# 🙌 Acknowledgements

- Google AI Studio (Gemini Flash)
- FAISS
- Sentence Transformers
- Streamlit Community
