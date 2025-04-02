---
title: AI Research Assistant
emoji: 🧠
colorFrom: indigo
colorTo: pink
sdk: streamlit
sdk_version: "1.31.1"
app_file: app.py
pinned: false
---

[![Hugging Face](https://img.shields.io/badge/🚀%20Live%20Demo-HuggingFace-blue?style=for-the-badge)](https://huggingface.co/spaces/arnob47/ai-research-assistant)

# 🧠 AI Research Assistant

An autonomous research assistant built with Streamlit, Transformers, and SerpAPI.  
This app takes a research topic, searches the web, scrapes content, summarizes articles using an AI model, and generates a downloadable report in both **Markdown** and **PDF** formats.

---

## ✨ Features

- 🔎 Web search using [SerpAPI](https://serpapi.com/)
- 🌐 Content scraping with BeautifulSoup
- 🧠 Summarization using Hugging Face Transformers (`facebook/bart-large-cnn`)
- 📄 Export to Markdown & PDF
- ⚡ Easy-to-use Streamlit interface
- 🌍 Live demo hosted on Hugging Face Spaces

---

## 📸 Demo

https://huggingface.co/spaces/arnob47/ai-research-assistant

---

## 📦 Tech Stack

- Python 3.10+
- [Streamlit](https://streamlit.io/)
- [Transformers](https://huggingface.co/docs/transformers/)
- [fpdf](https://py-pdf.github.io/fpdf2/)
- [SerpAPI](https://serpapi.com/)
- Hugging Face Spaces

---

## 🚀 How to Run Locally

### 🔧 Prerequisites

- Python 3.10 or higher
- [pip](https://pip.pypa.io/)
- A SerpAPI key → [Get one free](https://serpapi.com/)

---

### 🧪 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/aalexandros47/ai-projects/ai-research-assistant
cd ai-research-assistant

# 2. Create and activate a virtual environment (recommended)
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your SerpAPI key to .env
echo SERPAPI_KEY=your_key_here > .env

# 5. Run the app
streamlit run app.py
