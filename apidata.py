from dotenv import load_dotenv
import requests
import json

load_dotenv()
api_key = os.getenv('API_KEY')

def get_headlines(pageSize):
    res = requests.get(f"https://newsapi.org/v2/top-headlines?category=technology&pageSize={pageSize}&apiKey={api_key}")
    string = json.dumps(res.json())
    headlines = json.loads(string)
    return headlines['articles']


def article_details(n):
    name = articles[n]['source']['name']
    author = articles[n]['author']
    title = articles[n]['title']
    url = articles[n]['url']
    return name,author,title,url

