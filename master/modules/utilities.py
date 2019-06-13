
# Dictonaries

# En este momento no se usan

def homepage_dictionary(list_of_dics):

    """"Funcion que prepara el diccionario del homepage para hacer la tabla
    en html con la funcion generate_html_table"""

    keys = ['Title', 'Episode ID', 'Release Date', 'Director', 'Producers']
    dict = {}

    # Lista vacia en cada item
    for key in keys:
        dict[key] = []

    for movie in list_of_dics:

        dict['Title'].append(movie['title'])
        dict['Episode ID'].append(movie['episodeID'])
        dict['Release Date'].append(movie['releaseDate'])
        dict['Director'].append(movie['director'])
        dict['Producers'].append(', '.join(movie['producers']))

    return dict


# Generating tables for html

def generate_html_table(pixels, dict):

    """"Funcion que genera una tabla simple en html a partir de un diccionario
    con keys de los titulos de cada columna de la tabla y values una lista de
    cada elemento de la columna"""

    keys = dict.keys()
    length = len(dict[list(dict.keys())[0]])

    items = ['<table style="width:{}px">'.format(pixels), '<tr>']

    # Table titles
    for k in keys:
        items.append('<th align="left"> %s </th>' % k)

    items.append('</tr>')

    # Table contents
    for i in range(length):

        items.append('<tr>')

        for k in keys:
            items.append('<td>%s</td>' % dict[k][i])
        items.append('</tr>')

    items.append('</table>')

    return '\n'.join(items)
