# 📄 RAG avec FAISS + Qwen-3B (Streamlit)
<p align="left">
  <img src="https://github.com/user-attachments/assets/ba1f719c-8b27-4554-95cd-db5f3a620076" width="500"/>
</p>
Cette application Streamlit permet de :

- Extraire le texte d’un fichier PDF,
- Découper ce texte en morceaux (chunks) de 300 caractères,
- Indexer ces morceaux avec FAISS pour une recherche rapide par similarité,
- Utiliser le modèle de génération de texte Qwen-3B pour répondre à des questions basées sur le contenu du PDF.

---

## Fonctionnalités

- Téléversement de fichiers PDF
- Extraction et segmentation du texte
- Indexation vectorielle avec FAISS
- Recherche contextuelle intelligente
- Génération de réponses en langage naturel avec Qwen-3B

---

## Prérequis

- Python 3.8+
- Streamlit
- Faiss
- Transformers
- Sentence Transformers
- PyPDF

---

