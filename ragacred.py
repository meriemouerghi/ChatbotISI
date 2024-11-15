# -*- coding: utf-8 -*-
"""RAGAcred.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12IASDvsQu0WWOBZcGPoDd3L3z9CnCyC2
"""

! pip install -q --upgrade google-generativeai langchain-google-genai chromadb pypdf

# Commented out IPython magic to ensure Python compatibility.
# Install the Langchain which is a versatile framework designed to streamline the creation of applications driven by generative AI
!pip install -q langchain
# Install the OpenAI library, which provides access to OpenAI's powerful language models and APIs.
!pip install -q openai
# Install faiss-cpu (Facebook AI Similarity Search), a library for efficient similarity search and clustering of dense vectors.
!pip install -q faiss-cpu
# Install tiktoken, which is a Python library for counting the number of tokens in a text string without making API requests. We will use it in the OpenAI's API token usage monitoring.
!pip install -q tiktoken
# Install PyMuPDF, a Python library for working with PDF documents. We will use to extract text from PDFs.
!pip install -q PyMuPDF
# Install docx2txt, a library for extracting text from Microsoft Word (.docx) documents. Useful for text extraction and analysis from Word files.
!pip install -q docx2txt
!pip install -q langchain-community
!pip install llama-index 'google-generativeai>=0.3.0' matplotlib
# %pip install llama-index-embeddings-gemini
!pip3 install sentence_transformers
!pip install fitz

from IPython.display import display
from IPython.display import Markdown
import textwrap


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

import google.generativeai as genai
from google.colab import userdata

from google.colab import userdata
# The gemini api key
GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')
print(GOOGLE_API_KEY)

genai.configure(api_key=GOOGLE_API_KEY)

"""Text generation"""

model = genai.GenerativeModel(model_name = "gemini-pro")
model

"""Using langChain to Access Gemini API"""

!pip install google-generativeai --upgrade

"""**Processing Documents with RAG**"""

!sudo apt -y -qq install tesseract-ocr libtesseract-dev

!sudo apt-get -y -qq install poppler-utils libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig

!pip install langchain langchain-community

import urllib
import warnings
from pathlib import Path as p
from pprint import pprint

import pandas as pd
from langchain import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA



warnings.filterwarnings("ignore")
# restart python kernal if issues with langchain import.

!pip install --upgrade google-generativeai

!pip install langchain-google-genai

from langchain_google_genai import ChatGoogleGenerativeAI

!pip install chromadb python-dotenv

from google.colab import userdata
# The gemini api key
GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')
print(GOOGLE_API_KEY)

model = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=GOOGLE_API_KEY,
                             temperature=0.2,convert_system_message_to_human=True)

from google.colab import drive
drive.mount('/content/drive')

pip install pypdf

import os
from langchain.document_loaders import PyPDFLoader

# Chemin du dossier principal contenant les fichiers PDF
root_folder = '/content/drive/MyDrive/Accreditation'  # Remplacez avec le chemin vers votre dossier

# Liste pour stocker le contenu de tous les PDFs
all_pages = []

# Parcourir tous les fichiers PDF dans le dossier racine
for filename in os.listdir(root_folder):
    if filename.lower().endswith('.pdf'):  # Vérifie si le fichier est un PDF
        pdf_path = os.path.join(root_folder, filename)
        print(f"Chargement du fichier PDF : {pdf_path}")

        try:
            # Charger le PDF avec PyPDFLoader et diviser en pages
            pdf_loader = PyPDFLoader(pdf_path)
            pages = pdf_loader.load_and_split()

            # Ajouter toutes les pages du PDF à la liste all_pages
            all_pages.extend(pages)
            print(f"Ajouté {len(pages)} pages de {filename}.")

        except Exception as e:
            print(f"Erreur lors du chargement de {filename}: {e}")

# Afficher un aperçu des pages extraites
for i, page in enumerate(all_pages[:5]):  # Affiche les 5 premières pages pour un aperçu
    print(f"Page {i+1} :\n{page.page_content}\n{'-' * 40}")

import os
from langchain.document_loaders import PyPDFLoader

# Chemin du dossier principal sur Google Drive
root_folder = '/content/drive/MyDrive/Dossier_Accreditation CTI_ISI_2024__'  # Remplacez avec le chemin vers votre dossier principal

# Liste pour stocker le contenu de tous les PDFs
all_pages = []

# Parcourir récursivement tous les sous-dossiers et fichiers dans le dossier
for folder_name, subfolders, filenames in os.walk(root_folder):
    for filename in filenames:
        if filename.lower().endswith('.pdf'):  # Vérifie si le fichier est un PDF
            pdf_path = os.path.join(folder_name, filename)
            print(f"Chargement du fichier PDF : {pdf_path}")

            # Charger le PDF avec PyPDFLoader et diviser en pages
            pdf_loader = PyPDFLoader(pdf_path)
            pages = pdf_loader.load_and_split()

            # Ajouter toutes les pages du PDF à la liste all_pages
            all_pages.extend(pages)

# Afficher un aperçu des pages extraites
for i, page in enumerate(all_pages[:5]):  # Affiche les 5 premières pages pour un aperçu
    print(f"Page {i+1} :\n{page.page_content}\n{'-' * 40}")

"""Extract text from PDF

# RAG Pipeline: Embedding + Gemini
"""

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

import chromadb

chroma_client = chromadb.PersistentClient(path=r"/content/chroma_db")

collection = chroma_client.get_or_create_collection(name="tutorial",metadata={"hnsw:space": "cosine"})

from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb




# Initialisation de l'outil de découpe de texte
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=100)

# Créer un contexte combiné à partir de toutes les pages
context = "\n\n".join(str(p.page_content) for p in all_pages)
texts = text_splitter.split_text(context)

# Préparer les documents, métadonnées et ids pour ChromaDB
documents = []
metadata = []
ids = []
i = 0
# Parcourir chaque chunk de texte découpé
for i, chunk in enumerate(texts):
    documents.append(chunk)  # Ajouter directement le texte découpé
    ids.append("ID" + str(i))  # Créer un ID unique pour chaque chunk

    # Calculer le numéro de page approximatif, ajuster si nécessaire
    page_number = i // len(texts) * len(all_pages) + 1  # Ajustez ce calcul si nécessaire



    metadata.append({
        "source": "/A.4 Politique_ISI.pdf",  # Utilisation dynamique du nom du fichier
        "chunk_index": i,     # L'ordre du chunk
        "page_number": page_number,  # Numéro approximatif de la page
        "timestamp": "2024-11-11"  # Exemple de timestamp, à adapter si nécessaire
    })

# Assurez-vous que vous avez une collection ChromaDB disponible
chroma_client = chromadb.PersistentClient(path="/content/chroma_db")
collection = chroma_client.get_or_create_collection(name="tutorial")

collection.upsert(
    documents=documents,
    metadatas=metadata,
    ids=ids
)

print("Documents et métadonnées ajoutés avec succès à ChromaDB.")

for i, chunk in enumerate(texts):
    print(f"Chunk {i + 1} (Length: {len(chunk)}):\n{chunk}\n{'-' * 50}\n")

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=GOOGLE_API_KEY)


vector_index = Chroma.from_texts(
    texts=documents,                    # List of text chunks
    embedding=embeddings,               # Embedding model instance
    metadatas=metadata,                 # List of metadata for each document
)

vector_index = Chroma.from_texts(texts, embeddings).as_retriever(search_kwargs={"k":7})

qa_chain = RetrievalQA.from_chain_type(
    model,
    retriever=vector_index,
    return_source_documents=True,
    chain_type="refine",


)

def remove_repeated_phrases(text):
    # Split the text into sentences
    sentences = text.split(".")
    seen_sentences = set()
    filtered_sentences = []

    for sentence in sentences:
        if sentence.strip() not in seen_sentences:
            filtered_sentences.append(sentence.strip())
            seen_sentences.add(sentence.strip())

    # Join the filtered sentences back into a single response
    return ". ".join(filtered_sentences).strip() + "."

from langdetect import detect

# Détecter la langue de la question
question = "what is IDISC?"
langue_question = detect(question)

# Définir les paramètres de langue pour le modèle
if langue_question == 'fr':
    model_lang_param = 'fr'
elif langue_question == 'en':
    model_lang_param = 'en'
else:
    model_lang_param = 'fr'  # Défaut francais si langue inconnue

# Passer la question avec la langue au modèle, mais sans modifier la question affichée
result = qa_chain({
    "query": question,
    "language": model_lang_param  # Passer la langue comme paramètre interne
})

# Filtrer la réponse pour enlever les répétitions
filtered_answer = remove_repeated_phrases(result["result"])


print(filtered_answer)
question = "comment accèder au ingénierie?"
result = qa_chain({"query": question})

# Filtrer la réponse pour enlever les répétitions
filtered_answer = remove_repeated_phrases(result["result"])

print("Réponse affinée :")
print(filtered_answer)

question = "quel est la déclaration sociale et environnementale de l'ISI ?"
result = qa_chain({"query": question})
result["result"]

"""

> Add blockquote

"""

# Display the answer and the source documents (chunks used)
answer = result["result"]
source_chunks = result["source_documents"]

print("Answer:")
print(answer)
print("\nSource Chunks Used:")

# Print each source chunk and its content
for i, doc in enumerate(source_chunks):
    print(f"Chunk {i + 1}:\n{doc.page_content}\n{'-' * 50}")