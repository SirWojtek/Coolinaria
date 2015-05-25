from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist 
from django.views.decorators.csrf import csrf_exempt
from ingredient.models import Ingredient
import json

# @csrf_exempt
def ingredientIndex(request):
    if request.method == 'GET':
        return _getIngredients()
    elif request.method == 'POST':
        data = json.loads(request.POST['ingredient'])
        ingredient = _findIngredient(data)

        if ingredient:
            return _editIngredient(ingredient, data)
        else:
            return _addIngredient(data, request)

def _getIngredients():
    ingredients = []

    for ing in Ingredient.objects.all():
        ingredients.append(ing.getDict())

    return HttpResponse(json.dumps(ingredients),
        content_type = "application/json", status = 200)

def _findIngredient(data):
    try:
        ingredient = Ingredient.objects.get(name = data['name'])
    except ObjectDoesNotExist:
        return None
    return ingredient

def _editIngredient(ingredient, data, request):
    try:
        ingredient.image = request.FILES.itervalues().next()
        ingredient.isSearchable = data['searchable']
        ingredient.save()
    except Exception as e:
        print e
        return HttpResponse(status = 221)
    return HttpResponse(status = 200)

def _addIngredient(data, request):
    try:
        ingredient = Ingredient.objects.create(
            name = data['name'],
            image = request.FILES.itervalues().next(),
            isSearchable = data['searchable'])
    except Exception as e:
        print e
        return HttpResponse(status = 221)
    return HttpResponse(status = 200)

def _loadImage(request, filename):
    path = 'media/ingredients/' + filename
    with open(path, 'wb+') as dest:
        for chunk in request.FILES.itervalues().next().chunks():
            dest.write(chunk)
    return path

# unused method kept just in case
def deleteIngredient(request):
    if request.method != 'POST':
        return HttpResponse(status = 501)

    try:
        data = json.loads(request.body)
        ingredient = Ingredient.objects.get(name = data['name'])
        ingredient.delete()
    except DoesNotExist:
        HttpResponse(status = 220)
    except Exception as e:
        print e
        return HttpResponse(status = 221)
    return HttpResponse(status = 200)

def topIngredients(request):
    if request.method != 'GET':
        return HttpResponse(status = 501)

    return _getTiledIngredients()

def _getTiledIngredients():
    ingredients = []

    for ing in Ingredient.objects.all():
        ingredients.append(ing.getTiledDict())

    ingredients = sorted(ingredients, key = lambda k : k['displays'], reverse = True)

    return HttpResponse(json.dumps(ingredients),
        content_type = "application/json", status = 200)

def statsDisplayAll(request):
    if request.method != 'GET':
        return HttpResponse(status = 501)
    return _createHistogram()

def statsDisplay(request, count):
    if request.method != 'GET':
        return HttpResponse(status = 501)
    return _createHistogram(int(count))

def _createHistogram(count = -1):
    result = []
    i = 0
    
    for ing in Ingredient.objects.all():
            result.append(ing.getStatDict())

    result = sorted(result, key = lambda k : k['value'], reverse = True)
    if count != -1:
        result = result[:count]

    return HttpResponse(json.dumps(result))
