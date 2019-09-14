import requests
import json
import re
import sys
from bs4 import BeautifulSoup

def get_topic(url):
    match = re.search('https://(.+?)\.onliner\.by', url)
    topic = match.group(1)
    return topic

def get_news_id(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features='html.parser')
    news_id = soup.find('span', {'class': 'news_view_count'})['news_id']
    return news_id

url = sys.argv[1]

topic = get_topic(url)
news_id = get_news_id(url)
print(news_id)
comments_url = "https://comments.api.onliner.by/news/" + topic + ".post/" + str(news_id) + "/comments"

r = requests.get(comments_url)
comments_decoded = json.loads(r.text)

best = comments_decoded['pins']['best']
print(best)
