from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
api_key = os.getenv('API_KEY')

def get_headlines(category,pageSize):
    try:
         res = requests.get(f"https://newsapi.org/v2/top-headlines?category={category}&pageSize={pageSize}&apiKey={api_key}")
         string = json.dumps(res.json())
         headlines = json.loads(string)
         return headlines['articles']
    except Exception as e:
         print(e) 

def search_headline(query):
    try:
        res = requests.get(f"https://newsapi.org/v2/everything?qInTitle={query}&pageSize=4&sortBy=relevancy&apiKey={api_key}")
        string = json.dumps(res.json())
        headlines = json.loads(string)
        return headlines['articles']
    except Exception as e:
        print(e) 

# def article_details(n):
#     name = articles[n]['source']['name']
#     author = articles[n]['author']
#     title = articles[n]['title']
#     url = articles[n]['url']
#     return name,author,title,url

if __name__ == "__main__":
     print(get_headlines("sports","1"))
