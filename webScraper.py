import requests
from bs4 import BeautifulSoup

url = "https://www.thehindu.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# Extracting headlines
headlines = soup.find_all('h3', class_='title')

# Saving to file
with open("headlines.txt", "w", encoding='utf-8') as file:
    for i, headline in enumerate(headlines, start=1):
        text = headline.text.strip()
        if text:
            file.write(f"{i}. {text}\n")

print("Headlines successfully saved to headlines.txt")
