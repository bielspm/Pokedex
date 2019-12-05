from django.shortcuts import render,HttpResponse,Http404
from pokedexs.models import Pokemon
def index(request):
    return render(request,'pokedexs/index.html')

def resultado(request):
    if request.method == 'GET':
        resultados = Pokemon.objects.filter(pokemon_name=request.GET['user_input_str'])
        if resultados:
            return render(request,'pokedexs/resultado.html',{'resultados':resultados})
        else:
            raise Http404
    else:
        pokemon = Pokemon.objects.get(pokemon_number=request.POST['user_input_number'])
        if pokemon:
            return render(request, 'pokedexs/resultado.html', {'pokemon': pokemon})
        else:
            raise Http404

def pokemon(request,pokemon_id):
    pokemon = Pokemon.objects.get(pokemon_number=pokemon_id)
    pok_id_full = ''
    lendario = ''

    if pokemon.pokemon_number < 10:
        pok_id_full = '00'+f'{pokemon.pokemon_number}'
    if 10 <= pokemon.pokemon_number < 100:
        pok_id_full = '0'+f'{pokemon.pokemon_number}'
    if pokemon.pokemon_number > 100:
        pok_id_full = pokemon.pokemon_number
    if pokemon.is_legendary == 0:
        lendario = 'não'
    if pokemon.is_legendary == 1:
        lendario = 'sim'

    contexto = {'pok_id_full':pok_id_full,'pokemon':pokemon,'lendario':lendario}
    return render(request,'pokedexs/pokemon.html',contexto)
