import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/')

conteudo = response.content

site = BeautifulSoup(conteudo, 'html.parser')

noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:

    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

    subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})

    if(subtitulo):
        lista_noticias.append([titulo.text, subtitulo, titulo['href']])
    else:
        lista_noticias.append([titulo.text,'(Notícia sem título)', titulo['href']])

tabelaNoticia = pd.DataFrame(lista_noticias, columns=['Título', 'Subtítulo', 'Link'])

tabelaNoticia.to_excel('noticias.xlsx', index=False)



