import requests
from serpapi import GoogleSearch
from config import SERP_API_KEY


class NewsRetriever:
    def __init__(self):
        self.api_key = SERP_API_KEY

    def fetch_news(self, security_ticker):
        if not self.api_key:
            raise ValueError("SERP_API_KEY is not set")

        params = {
            "engine": "google_news",
            "q": security_ticker,
            "api_key": self.api_key,
            # "gl": "us",
            "hl": "en"
        }
        try:
            # search = google_search(params)
            search = GoogleSearch(params)
            results = search.get_dict()
            results = results.get('news_results', [])
            return results
        except Exception as e:
            print(f"Error retrieving news for {security_ticker}: {e}")
            return []

    def fetch_article_content(self, url):

        # Remove protocol if present
        if url.startswith("https://"):
            url = url[len("https://"):]
        elif url.startswith("http://"):
            url = url[len("http://"):]
        full_url = f"https://r.jina.ai/{url}"

        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Error fetching content for URL {full_url}: Status code {response.status_code}")
                return ""
        except Exception as e:
            print(f"Error fetching content for URL {full_url}: {e}")
            return ""
