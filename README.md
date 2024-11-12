# ChatbotISI
Développement d'un chatbot universaitre en utulisant RAG (NLP+LLM)
# Hackathon
Ce projet consiste en la création d'un chatbot RAG (Retrieval-Augmented Generation) intégré dans le site web. Il vise à faciliter le découpage, l'indexation et la recherche de contenu sur plusieurs types de documents (PDF, images, CSV, etc.) grâce à des fonctionnalités avancées de traitement du langage naturel (NLP) et d'accessibilité. Le projet utilise un frontend en Vue.js, un backend en Flask, et un système RAG pour garantir la pertinence des réponses.

# Fonctionnalités Principales
- Le managment de l'institut : Son pilotage,son fonctionnement et son systéme qualité
- La formation d'ingénieurs
- Le recrutement  des élèves ingénieurs
- La vie estudiante et la vie associative des éleves

# Détails des fonctionnalités

1. Découpage de texte et extraction de contenu
- Feature : Découpage du contenu des documents PDF en morceaux de texte, avec conservation de la structure et extraction par page.
Pôle Technologique : Traitement du langage naturel (NLP), Chargement et manipulation de documents.
- Outils : PyPDFLoader, RecursiveCharacterTextSplitter.
- Description : Utilisation d'un découpeur de texte pour segmenter le contenu en parties de longueur fixe avec chevauchement pour maintenir le contexte. Ce découpage est utilisé pour optimiser l'indexation et la recherche.
2. Préparation des métadonnées et indexation
- Feature : Génération de métadonnées associées à chaque segment de texte, incluant le numéro de page, la date et la source.
- Pôle Technologique : Systèmes de bases de données documentaires et gestion de métadonnées.
- Outils : ChromaDB pour stocker les documents et les métadonnées de manière persistante.
- Description : Chaque segment découpé est enrichi de métadonnées pour faciliter l'organisation et la recherche dans la base de données, ce qui améliore la précision des réponses pour les requêtes contextuelles.
3. Indexation vectorielle avec ChromaDB
- Feature : Création d'une collection ChromaDB avec des embeddings pour des requêtes efficaces.
- Pôle Technologique : Bases de données vectorielles, Recherche par similarité.
- Outils : ChromaDB, Embeddings de Google Gemini.
- Description : Les segments de texte sont convertis en vecteurs via des embeddings pour permettre une recherche basée sur la similarité sémantique, améliorant la pertinence des résultats.
4. Chaîne de question-réponse avec LangChain
- Feature : Utilisation d'une chaîne de question-réponse pour répondre aux questions de manière précise.
- Pôle Technologique : Modélisation et génération de texte, IA conversationnelle.
- Outils : LangChain, Google Gemini.
- Description : La question posée par l’utilisateur est traitée via un modèle génératif pour extraire une réponse contextuelle pertinente, en s'appuyant sur la recherche vectorielle.
5. Détection de la langue de la question
- Feature : Détection automatique de la langue pour générer des réponses dans la même langue.
- Pôle Technologique : Traitement du langage naturel (NLP), Détection de la langue.
- Outils : langdetect.
- Description : Le modèle détecte la langue d’entrée de la question (français ou anglais) et adapte la réponse en conséquence, assurant une expérience utilisateur cohérente.
6. Suppression des phrases répétées
- Feature : Filtrage des phrases répétitives dans les réponses pour les améliorer.
- Pôle Technologique : Traitement du texte, Nettoyage de données.
- Outils : Fonction de post-traitement personnalisée en Python.
- Description : Le texte généré par le modèle est nettoyé pour enlever les répétitions, afin de fournir des réponses claires et concises.
7. Conversion de texte en audio
- Feature : Lecture de la réponse en audio pour une meilleure accessibilité.
- Pôle Technologique : Synthèse vocale, Accessibilité numérique.
- Outils : gTTS (Google Text-to-Speech).
- Description : La réponse textuelle est convertie en audio, permettant aux utilisateurs d'écouter la réponse, une fonctionnalité précieuse pour l’accessibilité.

