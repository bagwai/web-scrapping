import requests
from bs4 import BeautifulSoup

url = 'https://www.premiumtimesng.com/news/585884-supreme-court-extends-old-naira-notes-validity-till-december.html'
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'lxml')

article = soup.find('div', {'class': 'entry-content'})

print(article.get_text())
