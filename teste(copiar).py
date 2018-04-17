import requests

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print(page.status_code)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

soup.prettify()


#[bs4.element.Doctype, bs4.element.NavigableString, bs4.element.Tag]
html = list(soup.children)[2]
print(list(html.children))
print("\n\n\n\n\n\n")

body = list(html.children)[3]
p = list(body.children)[1]



soup.find_all('p')
print(soup.find_all('p')[0].get_text())

print("\n\n")

#body = list(html.children)[3]
[print(type(item)) for item in list(soup.children)]


'''Agora nós podemos utilizar o método find_all para buscar por todos os itens por classe e id. No exemplo abaixo, vamos procurar por qualquer tag p que tenha a classe outer-text:


'''
soup.find_all('p', class_='outer-text')

soup.find_all(class_="outer-text")
''' Nós também podemos buscar elementos pela id.

1'''
soup.find_all(id="first")


