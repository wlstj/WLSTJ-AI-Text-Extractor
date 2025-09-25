from dotenv import load_dotenv
import os
import streamlit as st
from utils import extract_text, OPENAI_API_KEY, ask_ai, generate_flashcards

st.title("WLSTJ AI Text Extractor")

uploaded_file = st.file_uploader("Upload your note (PDF)", type=["pdf"])

if uploaded_file:
    st.success("PDF uploaded successfully")
    text = extract_text(uploaded_file)
    st.text_area("Extracted Notes", text, height=300)

    # if st.button("Ask AI about notes"):
    #     if not OPENAI_API_KEY:
    #         st.error("No OpenAI API Key found in .env")
    #     else:
    #         answer = ask_ai(question, text)
    #         st.subheader("AI Answer:")
    #         st.write(answer)
    #
    #
    # if st.button("Generate Flashcards"):
    #     if not OPENAI_API_KEY:
    #         st.error("No OpenAI API key found in .env")
    #     else:
    #         flashcards = generate_flashcards(text)
    #         st.subheader("Flashcards")
    #         st.write(flashcards)
load_dotenv()
