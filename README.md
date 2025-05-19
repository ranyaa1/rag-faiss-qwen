# 📄 RAG avec FAISS + Qwen-3B (Streamlit)
<p align="left">
  <img src="https://github.com/user-attachments/assets/ba1f719c-8b27-4554-95cd-db5f3a620076" width="500"/>
</p>

Cette application Streamlit permet d'extraire le contenu d'un fichier PDF, de l'indexer à l’aide de FAISS et d’interroger le contenu grâce au modèle de langage **Qwen-3B** déployé localement via **Ollama**.

## ✨ Fonctionnalités

- 📥 Téléversement de fichiers PDF
- 📚 Extraction et découpage intelligent du texte (par blocs de 300 caractères)
- 🔍 Indexation vectorielle avec FAISS pour une recherche sémantique rapide
- 🧠 Génération de réponses à des questions avec Qwen-3B (via Ollama)
- 🧹 Nettoyage automatique des balises `<think>` générées par le modèle

## 🛠️ Stack technique

- Python 3.10+
- [Streamlit](https://streamlit.io/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Sentence Transformers](https://www.sbert.net/)
- [Ollama](https://ollama.com/)
- Modèle utilisé : `qwen3:4b` (Qwen 3B compatible Ollama)

## 🚀 Lancer l’application

### 1. Démarrer Ollama avec le bon modèle :

```bash
ollama run qwen3:4b
