from dotenv import load_dotenv
import os
import pypdf
from openai import OpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def extract_text(file):
    pdf_reader = pypdf.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

def ask_ai(question, context):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "You are a helpful study assistant."},
            {"role": "user", "content": f"Notes:\n{context}\n\nQuestion: {question}"}
        ],
        max_tokens = 300
    )
    return response.choices[0].message.content

def generate_flashcards(context):
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "You are a flashcard generator."},
            {"role": "user", "content": f"Turn these notes into 5 random Q&A flashcards:\n{context}"}           
        ],
        max_tokens = 400
    )
    return response.choices[0].message.content