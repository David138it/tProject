import requests
from bs4 import BeautifulSoup
url = 'https://propertyhub.in.th/en/condo/bts-national-stadium'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
#quotes = soup.find_all('div', class_='eHFUYJ')
#properties = soup.find_all('p', class_='bDIOCI')
#tags = soup.find_all('div', class_='faQqlI')
#for i in range(0, len(quotes)):
    #print('--' + properties[i].text)
    #tagsforquote = tags[i].find_all('a')
    #for j in tagsforquote:
        #print(j.text)
    #print('++++++++++')
items = soup.find_all('div', class_='col-xs sc-1qj7qf1-2 sc-elaovb-2 hWmzkP eHFUYJ')
for n, i in enumerate(items, start=1):
    properties = i.find('p', class_='bDIOCI').text.strip()
    for j in range(0, len(items)):
        print('--' + items[j].text)
    #itemPrice = i.find('div', class_='sc-p50xz0-10 faQqlI').text
    #print(f'{n}:  {itemPrice} за {properties}')
