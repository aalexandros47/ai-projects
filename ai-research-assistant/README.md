```markdown
# 🧠 AI Research Assistant

**Live Demo 👉 [Hugging Face Space](https://huggingface.co/spaces/arnob47/ai-research-assistant)**

A lightweight autonomous research assistant powered by **Streamlit**, **Hugging Face Transformers**, **SerpAPI**, and **BeautifulSoup**. It searches the web for relevant articles, scrapes them, summarizes the content using NLP, and generates a downloadable research report in Markdown format.

---

## 🚀 Features

- 🔎 Searches the web using SerpAPI (Google Search engine)
- 🧽 Scrapes article content using BeautifulSoup
- 🤖 Summarizes with Hugging Face BART (`facebook/bart-large-cnn`)
- 📄 Downloads clean, structured markdown reports
- 🖥️ Simple and beautiful Streamlit interface

---

## 💡 How It Works

1. Enter a research query like `"History of Artificial Intelligence"`
2. The app searches the web and fetches the top 3 relevant links
3. Scrapes content from those links (HTML parsing)
4. Summarizes each using Hugging Face's `facebook/bart-large-cnn`
5. Organizes results into a Markdown report
6. Previews and downloads the final report as `.md`

---

## 🧪 Run It Locally

### 🔁 1. Clone the Repository

```bash
git clone https://github.com/aalexandros47/ai-projects.git
cd ai-projects/ai-research-assistant
```

### 🛠️ 2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔑 4. Add Your SerpAPI Key

Create a `.env` file in the project root:

```env
SERPAPI_KEY=your_actual_serpapi_key_here
```

You can get your key from https://serpapi.com/manage-api-key

### ▶️ 5. Run the App

```bash
streamlit run app.py
```

Then open the browser at `http://localhost:8501`.

---

## 📝 Requirements

Make sure your `requirements.txt` includes:

```txt
streamlit
requests
beautifulsoup4
transformers
python-dotenv
```

---

## 📤 Output

- ✅ **Markdown Report**: A structured `.md` file containing the summarized results
- ✅ **Inline Preview**: See the generated report directly inside the app
- 🚫 **PDF Output Removed**: To avoid font issues on Hugging Face hosting

---

## 🌐 Optional: Hosting on Hugging Face Spaces

1. Create a new Space and set SDK to **Streamlit**
2. Push your project code to it
3. Set `SERPAPI_KEY` in Hugging Face → Settings → Secrets
4. Done! The app will auto-deploy ✨

---

## 👨‍💻 Author

**Arnob Ghosh**  
GitHub: [@aalexandros47](https://github.com/aalexandros47)

---

## 📜 License

This project is licensed under the MIT License — use it freely and responsibly.
```
