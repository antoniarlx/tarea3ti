from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .modules import my_requests

# Index Simple

# def index(request):
#     return HttpResponse("Hello, world. You're at the master index.")

def index(request):

    template = loader.get_template('master/index.html')
    list_of_dics = my_requests.homepage_movies_request()

    context = {'movies_dic': list_of_dics}
    for dic in list_of_dics:
        dic['producers'] = ', '.join(dic['producers'])

    return HttpResponse(template.render(context, request))

def movie_info(request, id):

    template = loader.get_template('master/movie_info.html')

    # Get info of clicked movie
    dict = my_requests.movie_info_request(id)

    # Arrange info for display
    dict['producers'] = ', '.join(dict['producers'])
    dict['created'] = dict['created'][:10]
    dict['edited'] = dict['edited'][:10]

    # Diccionaries of characters, planets and starships
    characters = dict['characterConnection']['characters']
    starships = dict['starshipConnection']['starships']
    planets = dict['planetConnection']['planets']

    context = {'movie_dic': dict, 'characters': characters,
                'starships': starships, 'planets': planets}

    return HttpResponse(template.render(context, request))

def characters(request, id):

    template = loader.get_template('master/characters.html')

    # Get info of clicked character
    dict = my_requests.character_info_request(id)

    dict['created'] = dict['created'][:10]
    dict['edited'] = dict['edited'][:10]

    homeworld = dict['homeworld']
    films = dict['filmConnection']['films']
    starships = dict['starshipConnection']['starships']

    context = {'character_dic': dict,
                'homeworld': homeworld,
                'starships': starships,
                'films': films}

    return HttpResponse(template.render(context, request))

def starships(request, id):

    template = loader.get_template('master/starships.html')

    # Get info of clicked starship
    dict = my_requests.starship_info_request(id)

    dict['created'] = dict['created'][:10]
    dict['edited'] = dict['edited'][:10]

    dict['manufacturers'] = ', '.join(dict['manufacturers'])
    films = dict['filmConnection']['films']
    pilots = dict['pilotConnection']['pilots']

    context = {'starship_dic': dict,
                'films': films,
                'pilots': pilots}

    return HttpResponse(template.render(context, request))

def planets(request, id):

    template = loader.get_template('master/planets.html')

    # Get info of clicked planet
    dict = my_requests.planet_info_request(id)

    dict['created'] = dict['created'][:10]
    dict['edited'] = dict['edited'][:10]

    dict['climates'] = ', '.join(dict['climates'])
    dict['terrains'] = ', '.join(dict['terrains'])

    films = dict['filmConnection']['films']
    residents = dict['residentConnection']['residents']

    context = {'planet_dic': dict,
                'films': films,
                'residents': residents}

    return HttpResponse(template.render(context, request))
