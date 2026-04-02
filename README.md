# 🤖 AI Resume Analyzer

> **An intelligent, NLP-powered web application that matches resumes to job descriptions — giving candidates a competitive edge with AI-driven insights.**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?style=flat-square&logo=streamlit)
![NLP](https://img.shields.io/badge/NLP-NLTK-green?style=flat-square)
![ML](https://img.shields.io/badge/ML-Sentence--Transformers-orange?style=flat-square)
[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)](LICENSE)

---

## 📌 Overview

**AI Resume Analyzer** is a machine learning project that bridges the gap between candidates and job opportunities. By leveraging state-of-the-art Natural Language Processing (NLP) and sentence embeddings, it compares a resume against a job description and produces a semantic match score — along with actionable feedback to help candidates tailor their applications.

Whether you're a job seeker optimizing your resume or a developer exploring applied NLP, this project demonstrates practical ML in a clean, interactive interface.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 **PDF Resume Upload** | Parse and extract text from uploaded PDF resumes |
| 🧠 **NLP Preprocessing** | Clean, tokenize, and normalize text using NLTK |
| 🤖 **Semantic Similarity Matching** | Compute deep embeddings via Sentence Transformers |
| 📊 **Match Score (0–100%)** | Quantified similarity between resume and job description |
| 💡 **AI-Powered Suggestions** | Smart, score-based feedback to improve resume relevance |
| 🌐 **Interactive Web Interface** | Fast, user-friendly UI built with Streamlit |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.9+ |
| **NLP** | NLTK |
| **Embeddings** | Sentence Transformers (`all-MiniLM-L6-v2`) |
| **Similarity** | Scikit-learn (Cosine Similarity) |
| **Web App** | Streamlit |
| **PDF Parsing** | PyMuPDF / pdfplumber |

---

## 📂 Project Structure

```
ai-resume-analyzer/
│
├── data/                   # Sample datasets and test resumes
├── src/                    # Core ML and NLP logic
│   ├── parser.py           # PDF text extraction
│   ├── preprocessor.py     # Text cleaning and normalization
│   └── matcher.py          # Embedding generation and similarity scoring
│
├── app/
│   └── streamlit_app.py    # Main Streamlit web application
│
├── models/                 # Saved or cached model files
├── notebooks/              # Jupyter notebooks for experimentation
│
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip package manager

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/PrashantSinghpns/ai-resume-analyzer.git
cd ai-resume-analyzer
```

**2. Create and activate a virtual environment** *(recommended)*
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Download NLTK data** *(first-time setup)*
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### Running the App

```bash
streamlit run app/streamlit_app.py
```

Then open your browser and navigate to `http://localhost:8501`.

---

## 🧪 How It Works

```
User uploads PDF Resume
        │
        ▼
  Text Extraction (PyMuPDF / pdfplumber)
        │
        ▼
  NLP Preprocessing (NLTK)
  → Tokenization → Stopword Removal → Lemmatization
        │
        ▼
  Sentence Embeddings (Sentence Transformers)
  → Resume Vector  |  Job Description Vector
        │
        ▼
  Cosine Similarity Score (Scikit-learn)
        │
        ▼
  Match Score (0–100%) + AI Feedback
```

---

## 🏁 Project Milestones

### ✅ Milestone 1 — Project Foundation
> *Laying the groundwork for everything that follows.*

Set up the complete project structure — organized directories for source code, data, models, and notebooks. Configured the Python environment, installed all core dependencies, and initialized the GitHub repository with a clean, scalable architecture ready for development.

---

### ✅ Milestone 2 — Resume Ingestion Engine
> *The app can now read and understand a PDF resume.*

Built the PDF parsing pipeline that accepts an uploaded resume, extracts raw text content page by page, and handles edge cases like multi-column layouts and embedded fonts. This forms the data entry point of the entire analysis pipeline.

---

### 🔄 Milestone 3 — NLP Preprocessing Pipeline *(In Progress)*
> *Turning raw text into clean, meaningful data.*

Implementing text preprocessing using NLTK — including tokenization, stopword removal, punctuation stripping, and lemmatization. This step transforms noisy resume and job description text into normalized tokens that the ML model can meaningfully compare.

---

### ⏳ Milestone 4 — Semantic Embedding Layer
> *Teaching the app to understand meaning, not just words.*

Will integrate Sentence Transformers (`all-MiniLM-L6-v2`) to convert both the resume and job description into high-dimensional semantic vectors. Unlike keyword matching, this approach captures the *meaning* behind phrases — so "built REST APIs" and "developed backend services" register as similar.

---

### ⏳ Milestone 5 — Similarity Scoring & Feedback Engine
> *Producing the score and telling the user what to improve.*

Will compute cosine similarity between the resume and job description vectors, producing a final match score from 0–100%. A rule-based feedback engine will then generate tailored suggestions — highlighting missing skills, weak sections, and keywords the resume should include.

---

### ⏳ Milestone 6 — Streamlit Web App & End-to-End Integration
> *Bringing everything together into a usable product.*

Will wire all components into a polished Streamlit interface — resume upload, live score display, visual feedback, and suggestions — making the tool accessible to non-technical users with zero setup required.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Please make sure your code follows the existing style and includes relevant comments.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [Sentence Transformers](https://www.sbert.net/) — for state-of-the-art semantic embeddings
- [NLTK](https://www.nltk.org/) — for robust NLP preprocessing
- [Streamlit](https://streamlit.io/) — for the rapid web app framework
- [Scikit-learn](https://scikit-learn.org/) — for similarity computation utilities

---

<p align="center">Built using Python & NLP</p>
