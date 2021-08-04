import requests as req
from bs4 import BeautifulSoup as BS

header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
url = "https://gammatest.net/course/python/"
full_page = req.get(url)

soup = BS(full_page.content, 'html.parser')
match = soup.find_all(string=True)
print(match)