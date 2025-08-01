import streamlit as st
import PyPDF2
import pyperclip  # Optional, for auto copy (won't work in browser-only Streamlit)

st.title("📄 AI-Powered Resume Analyzer (Free Version)")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    st.subheader("📃 Extracted Resume Text")
    st.text_area("Resume Content", text, height=300)

    if st.button("Copy Resume Text for AI"):
        st.code(text, language="text")
        st.success("✅ Text ready to copy! Use the prompt below.")

        st.markdown("""
        ### 🧠 Prompt to Use in ChatGPT:
        ```
        Act as a professional resume reviewer. Review the following resume and give:
        1. A brief summary
        2. Strengths
        3. Weaknesses
        4. Suggestions to improve (keywords, formatting, skills, grammar)

        Resume:
        [PASTE THE RESUME TEXT HERE]
        ```
        """)

        st.markdown("👉 Go to [ChatGPT Free](https://chat.openai.com/) and paste this prompt for AI feedback.")
