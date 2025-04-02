import os
from dotenv import load_dotenv
import requests

load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def search_web(query, max_results=3):
    print("🔍 Using SerpAPI to search for:", query)
    url = "https://serpapi.com/search.json"
    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "engine": "google",
        "num": max_results
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        results = []

        for result in data.get("organic_results", []):
            link = result.get("link")
            if link:
                results.append(link)
            if len(results) >= max_results:
                break

        return results
    except Exception as e:
        print("❌ Search error:", e)
        return []
