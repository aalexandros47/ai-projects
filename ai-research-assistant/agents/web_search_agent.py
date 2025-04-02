import os
import requests

# Try loading .env (optional on Hugging Face)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Get API key from environment or Hugging Face secrets
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

if not SERPAPI_KEY:
    raise ValueError("❌ SERPAPI_KEY not found. Please set it in your environment or Hugging Face secret variables.")

def search_web(query, max_results=3):
    print(f"🔍 Using SerpAPI to search for: {query}")
    
    url = "https://serpapi.com/search.json"
    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "engine": "google",
        "num": max_results
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise if not 200 OK
        data = response.json()

        results = []
        for result in data.get("organic_results", []):
            link = result.get("link")
            if link:
                results.append(link)
            if len(results) >= max_results:
                break

        if not results:
            print("❌ No links found. Try a different query.")

        return results

    except Exception as e:
        print(f"❌ Search error: {e}")
        return []