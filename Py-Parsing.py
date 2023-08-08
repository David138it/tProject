import requests
from bs4 import BeautifulSoup
url = 'https://propertyhub.in.th/en/condo/bts-national-stadium'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
blocks = soup.find_all('div', class_='col-xs sc-1qj7qf1-2 sc-elaovb-2 hWmzkP eHFUYJ')
properties = soup.find_all('p', class_='sc-elaovb-3 bDIOCI')
dist = soup.find_all('span', class_='distance')
#tags = soup.find_all('div', class_='sc-p50xz0-10 faQqlI')
#counts = soup.find_all('span', class_='sc-p50xz0-10 faQqlI')
for i in range(0, len(blocks)):
    #print(blocks[i].text
    print(properties[i].text)
    print(dist[i].text)
    print('++++++++++')
#block = soup.find_all('div', class_='sc-m8nysy-4 sc-m8nysy-5 gZMuCg bRKZIw')
#for n, i in enumerate(block, start=1):
#    print('++++++++++++'+i.text)
    #blocks = i.find('div', class_='col-xs sc-1qj7qf1-2 sc-elaovb-2 hWmzkP eHFUYJ').text.strip()
#items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
#for n, i in enumerate(items, start=1):
#    itemName = i.find('h4', class_='card-title').text.strip()
#    itemPrice = i.find('h5').text
#    print(f'{n}:  {itemPrice} за {itemName}')