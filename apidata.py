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

def get_articles_as_text(articles):
  # Getting news for n articles
  article_string="\n 🗞 Headlines🗞 \n"
  for n in articles:
    name = n['source']['name']
    author = n['author']
    title = n['title']
    url = n['url']
    article_string += f""" 
    📩 Title: {title}  
    ✒️ Author: {author} 
    🌐 Url: {url} 
    Provided By {name} 
    -------- """
  return article_string

if __name__ == "__main__":
     articles=get_headlines("technology","1")
     string = get_articles_as_text(articles) 
     print(string)
