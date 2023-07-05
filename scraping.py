print('We gaan scrapen')

import requests
from bs4 import BeautifulSoup

pagina = requests.get('https://coinmarketcap.com')

heelDeHtml = BeautifulSoup(pagina.content, 'html.parser')

body = heelDeHtml.find('tbody')
print(body.prettify())

print("changes")