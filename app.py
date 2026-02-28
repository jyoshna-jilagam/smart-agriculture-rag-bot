import streamlit as st
import google.generativeai as genai
import os

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="Smart Agriculture AI 🌾",
    page_icon="🌾",
    layout="centered"
)

# ==============================
# LOAD API KEY FROM SECRETS
# ==============================
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("API key not found. Add it in Streamlit Cloud Secrets.")
    st.stop()

genai.configure(api_key=api_key)

# ==============================
# MODEL
# ==============================
model = genai.GenerativeModel("gemini-1.5-flash-8b")

def generate_answer(question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception:
        return "⚠️ API quota exceeded or error occurred."

# ==============================
# CUSTOM CSS
# ==============================
st.markdown("""
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1500382017468-9049fed747ef");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.chat-box {
    background: rgba(0,0,0,0.6);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# SESSION STATE
# ==============================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ==============================
# UI
# ==============================
st.markdown('<div class="chat-box">', unsafe_allow_html=True)
st.title("🌾 Smart Agriculture Assistant")

for role, message in st.session_state.chat_history:
    if role == "user":
        st.markdown(f"**👩‍🌾 You:** {message}")
    else:
        st.markdown(f"**🤖 AI:** {message}")

user_input = st.text_input("Ask your agriculture question")

if st.button("Send"):
    if user_input.strip():
        st.session_state.chat_history.append(("user", user_input))
        answer = generate_answer(user_input)
        st.session_state.chat_history.append(("bot", answer))
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
