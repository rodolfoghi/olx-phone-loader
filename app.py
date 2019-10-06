from converter import gif_to_png, image_to_text
from file_helper import dictionary_list_to_csv
from util import get_site_html, get_bsobj_from

def get_anuncio(url_anuncio):
    print("Buscando " + url_anuncio)
    anuncio = {"url": url_anuncio}

    html_anuncio = get_site_html(url_anuncio)
    if html_anuncio is None:
        return None

    obj_anuncio = get_bsobj_from(html_anuncio)
    if obj_anuncio is None:
        return None

    span_visible_phone = obj_anuncio.find(id="visible_phone")
    span_codigo_do_anuncio = obj_anuncio.find("span", {"class": "sc-gqjmRU"})
    codigo_do_anuncio = span_codigo_do_anuncio.get_text()
    #print("Código do anúncio: " + codigo_do_anuncio)
    anuncio["codigo"] = codigo_do_anuncio
    phone = "Desconhecido"
    if (span_visible_phone):
        imgurl = span_visible_phone.img['src']

        img = get_site_html(imgurl)
        if img is None:
            return None

        gif_name = "images/" + codigo_do_anuncio + '.gif'
        localFile = open(gif_name, 'wb')
        localFile.write(img.read())
        localFile.close()
        gif_to_png(gif_name)
        phone = image_to_text(gif_name + '.png')

    anuncio["phone"] = phone
    return anuncio


def get_anuncios(url):
    html = get_site_html(url)
    if html is None:
        return None

    bsObj = get_bsobj_from(html)
    if bsObj is None:
        return None

    try:
        links_for_anuncios = bsObj.findAll("a", {"class": "OLXad-list-link"})
    except AttributeError as e:
        print("Erro ao obter lista de anúncios")
        print(e)
        return None

    anuncios = []
    for link_anuncio in links_for_anuncios:
        anuncio = get_anuncio(link_anuncio['href'])
        anuncios.append(anuncio)
        print(anuncio)
        print(" ")
    return anuncios

def run():
    url = ""

    while url == "":
        url = input("Informe a URL desejada: ")

    numero_de_paginas = input("Informe a quantidade de páginas: ")

    if numero_de_paginas == "":
        numero_de_paginas = 1
    else:
        numero_de_paginas = int(numero_de_paginas)

    anuncios = []

    for page in range(numero_de_paginas):
        pagina_atual = page + 1
        print("Obtendo anuncios da pagina " + str(pagina_atual))

        url_formatada = url
        if pagina_atual > 1:
            url_formatada += "&o=" + str(pagina_atual)

        anuncios_da_pagina = get_anuncios(url_formatada)
        anuncios.extend(anuncios_da_pagina)

    dictionary_list_to_csv(anuncios)

run()