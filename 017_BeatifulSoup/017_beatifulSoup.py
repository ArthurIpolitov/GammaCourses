import requests
from bs4 import BeautifulSoup as BS
import re

header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
url = "https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/maxmin-ohutemp/"

# https://www.google.com/search?q=eur+to+byn&oq=EUR+TO+BYN&aqs=chrome.0.0i512l2j0i22i30l8.2573j1j7&sourceid=chrome&ie=UTF-8

full_page = requests.get(url, headers=header)
soup = BS(full_page.content, 'html.parser')

# true_tags = soup.find_all(True)
# for tag in true_tags:
#     print(tag.name)

# new_soup = soup.find('tr')
# print(new_soup)
# print(new_soup.find_next('td'))

# print(soup.find('div', class_=''))

# exchange_rate = float(soup.find('span', class_= 'DFlfde SwHCTb')['data-value'])
#
# def main(rate):
#     user_choice = input('Please choose\n'
#                         '1. EUR to BYN\n'
#                         '2. BYN to EUR\n'
#                         '0. Exit\n'
#                         '----------------> ')
#
#     if user_choice == '1':
#         eur_to_byn(rate)
#     elif user_choice == '2':
#         byr_to_eur(rate)
#     elif user_choice == '0':
#         print('EXIT')
#         exit()
#     else:
#         print('OUT OF RANGE')
#         main(rate)
#
# def eur_to_byn(rate):
#     try:
#         amount = float(input('Please enter amount of EUR: '))
#     except:
#         print('ERROR')
#         eur_to_byn(rate)
#
#     else:
#         print(str(amount * rate) + " BYN")
#         main(rate)
#
# def byr_to_eur(rate):
#     try:
#         amount = float(input('Please enter amount of BYR: '))
#
#     except:
#         print('ERROR')
#         byr_to_eur(rate)
#
#     else:
#         print(str(amount / rate) + " EUR")
#         main(rate)
#
#
# main(exchange_rate)


contents = soup.find('tbody')

results = {}
for row in contents.find_all('tr'):
    row_data = row.find_all('td')
    results[row_data[0].text] = [row_data[1].text, row_data[2].text, row_data[3].text]


user_input = input('Name: ')
print(f'Maximum: {results[user_input][0]} and Minimum: {results[user_input][1]}')