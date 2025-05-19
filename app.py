import os
os.environ["USE_TF"] = "0"
import streamlit as st
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# === 1. Lire le PDF ===
def read_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

# === 2. Découper le texte en chunks de 300 caractères ===
def split_text(text, chunk_size=300):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# === 3. Indexer avec FAISS ===
def create_faiss_index(chunks, model):
    embeddings = model.encode(chunks)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index, embeddings

# === Streamlit UI ===
st.title("📄 RAG avec FAISS + Qwen-3B")

uploaded_file = st.file_uploader("📤 Téléverse ton fichier PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("📚 Lecture et traitement en cours..."):
        text = read_pdf(uploaded_file)
        chunks = split_text(text)

        embedder = SentenceTransformer('all-MiniLM-L6-v2')
        index, embeddings = create_faiss_index(chunks, embedder)

        tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-4B")
        model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen3-4B")
        generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

    st.success("✅ PDF indexé avec FAISS")

    query = st.text_input("❓ Pose ta question")

    if query:
        q_embedding = embedder.encode([query])
        D, I = index.search(np.array(q_embedding), k=3)
        context_raw = " ".join([chunks[i] for i in I[0]])

        prompt = f"Contexte : {context_raw}\nQuestion : {query}\nRéponse :"

        with st.spinner("🔍 Recherche de la réponse..."):
            output = generator(prompt, max_new_tokens=150)
            answer = output[0]['generated_text'].split("Réponse :")[-1].strip()

        st.markdown("### 🤖 Réponse")
        st.write(answer)
