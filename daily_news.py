import requests
from bs4 import BeautifulSoup

url = "https://www.arabnews.com/saudiarabia"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
headlines = soup.find("body").find_all("h4")

for x in headlines:
    print(x.text.strip())
