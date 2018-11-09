from urllib.request import urlopen
from bs4 import BeautifulSoup
from converter import gif_to_png, image_to_text
from file_helper import dictionary_list_to_csv

def get_anuncio(url_anuncio):
    #print("Buscando " + url_anuncio)
    anuncio = {"url": url_anuncio}
    html_anuncio = urlopen(url_anuncio)
    obj_anuncio = BeautifulSoup(html_anuncio.read(), "html.parser")
    span_visible_phone = obj_anuncio.find(id="visible_phone")
    div_codigo_do_anuncio = obj_anuncio.find("div", {"class": "OLXad-id"})
    codigo_do_anuncio = div_codigo_do_anuncio.p.strong.get_text()
    #print("Código do anúncio: " + codigo_do_anuncio)
    anuncio["codigo"] = codigo_do_anuncio
    phone = "Desconhecido"
    if (span_visible_phone):
        imgurl = span_visible_phone.img['src']
        img = urlopen(imgurl)
        gif_name = "images/" + codigo_do_anuncio + '.gif'
        localFile = open(gif_name, 'wb')
        localFile.write(img.read())
        localFile.close()
        gif_to_png(gif_name)
        phone = image_to_text(gif_name + '.png')

    anuncio["phone"] = phone
    return anuncio


def get_anuncios(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read(), "html.parser")

    links_for_anuncios = bsObj.findAll("a", {"class": "OLXad-list-link"})

    anuncios = []
    for link_anuncio in links_for_anuncios:
        anuncio = get_anuncio(link_anuncio['href'])
        anuncios.append(anuncio)
        print(anuncio)
        print(" ")
    return anuncios

def run():
    url = ""
    numero_de_paginas = 1
    anuncios = []

    for page in range(numero_de_paginas):
        pagina_atual = page + 1
        #print("Obtendo anuncios da pagina " + str(pagina_atual))
        anuncios_da_pagina = get_anuncios(url + str(pagina_atual))
        anuncios.extend(anuncios_da_pagina)

    dictionary_list_to_csv(anuncios)

run()

# def search_anuncios(url_pesquisada, pagina_inicial, pagina_final):
#     anuncios = []
#     if (pagina_inicial == 1):
#         pagina_inicial = 0

#     if (pagina_inicial == pagina_final):
#         pagina_final += 1

#     for pagina in range(pagina_inicial, pagina_final):
#         anuncios_da_pagina = get_anuncios(url_pesquisada + "&o=" + str(pagina))
#         anuncios.extend(anuncios_da_pagina)
#     return anuncios