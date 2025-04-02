import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = " ".join([para.get_text() for para in paragraphs])
        return text[:5000]
    except Exception as e:
        print("❌ Error scraping:", e)
        return ""
