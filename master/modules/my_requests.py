import requests

URL = 'https://swapi-graphql-integracion-t3.herokuapp.com/'
metodo = 'post'

def homepage_movies_request():

    """Hace un request de la informacion de las peliculas a mostrar en la
    primera pagina: title, episode, year, director, producers, more info"""

    query = """
                    {
                      allFilms {
                        edges {
                          node {
                            id
                            episodeID
                            title
                            director
                            producers
                            releaseDate
                          }
                        }
                      }
                    }
                """

    r = requests.post('https://swapi-graphql-integracion-t3.herokuapp.com/',
                      json={'query': query})

    data = r.json()

    list_of_dics = [data['data']['allFilms']['edges'][0]['node'],
                    data['data']['allFilms']['edges'][1]['node'],
                    data['data']['allFilms']['edges'][2]['node'],
                    data['data']['allFilms']['edges'][3]['node'],
                    data['data']['allFilms']['edges'][4]['node'],
                    data['data']['allFilms']['edges'][5]['node'],
                    data['data']['allFilms']['edges'][6]['node']]

    list = []
    for item in list_of_dics:
        list.append(item['id'])

    return list_of_dics


def movie_info_request(id):

    """Hace un request de la informacion de la pelicula correspondiente al id
    seleccionado, entregando toda la informacion requerida"""

    q1 = """
            {
              film(id:" """

    q2 = """") {
                id
                episodeID
                title
                openingCrawl
                releaseDate
                director
                producers
                created
                edited
                characterConnection {
                    characters {
                        name
                        id
                      }
                    }
                starshipConnection {
                    starships {
                        name
                        id
                      }
                    }
                planetConnection {
                    planets {
                        name
                        id
                      }
                    }
            }
        }
        """

    query = '{}{}{}'.format(q1, id, q2)

    r = requests.post('https://swapi-graphql-integracion-t3.herokuapp.com/',
                      json={'query': query})

    # DATA

    data = r.json()['data']['film']

    # Diccionario con llaves id, episode ID y etcetera.

    # Llaves [characterConnection][characters] llevan a lista de diccionarios
    # con dos llaves: name, id

    # Lista de diccionarios con dos llaves: name, id

    characters = data['characterConnection']['characters']
    starships = data['starshipConnection']['starships']
    planets = data['planetConnection']['planets']

    return data


def character_info_request(id):

    """Hace un request de la informacion de la persona correspondiente al id
    seleccionado, entregando toda la informacion requerida"""

    q1 = """{
                person(id: " """

    q2 = """") {
                    name
                    height
                    mass
                    hairColor
                    skinColor
                    eyeColor
                    birthYear
                    gender
                    created
                    edited
                    homeworld   {
                        name
                        id
                        }
                    filmConnection  {
                        films   {
                            title
                            id
                            }
                        }
                    starshipConnection  {
                        starships   {
                            name
                            id
                            }
                        }
                }
            }
            """

    query = '{}{}{}'.format(q1, id, q2)

    r = requests.post('https://swapi-graphql-integracion-t3.herokuapp.com/',
                      json={'query': query})

    data = r.json()['data']['person']

    return data


def planet_info_request(id):

    """Hace un request de la informacion del planeta correspondiente al id
    seleccionado, entregando toda la informacion requerida"""

    q1 = """

    {
            planet(id:" """

    q2 = """") {
                name
                rotationPeriod
                orbitalPeriod
                diameter
                climates
                gravity
                terrains
                surfaceWater
                population
                created
                edited

                filmConnection {
                  films {
                    title
                    id
                  }
                }

                residentConnection {
                  residents {
                    name
                    id
                  }
                }
                }
                }
                """

    query = '{}{}{}'.format(q1, id, q2)

    r = requests.post('https://swapi-graphql-integracion-t3.herokuapp.com/',
                      json={'query': query})

    data = r.json()['data']['planet']

    return data


def starship_info_request(id):

    """Hace un request de la informacion del starship correspondiente al id
    seleccionado, entregando toda la informacion requerida"""

    q1 = """
            {
                starship(id:" """

    q2 = """") {
                        name
                        model
                        manufacturers
                        costInCredits
                        length
                        maxAtmospheringSpeed
                        crew
                        passengers
                        cargoCapacity
                        consumables
                        hyperdriveRating
                        MGLT
                        starshipClass
                        created
                        edited

                        pilotConnection {
                          pilots {
                            name
                            id
                          }
                        }

                        filmConnection {
                          films {
                            title
                            id
                          }
                }
                }
                }
                """

    query = '{}{}{}'.format(q1, id, q2)

    r = requests.post('https://swapi-graphql-integracion-t3.herokuapp.com/',
                      json={'query': query})

    data = r.json()['data']['starship']

    return data
