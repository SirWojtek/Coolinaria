from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist 
from django.views.decorators.csrf import csrf_exempt
from ingredient.models import Ingredient
import json

@csrf_exempt
def ingredientIndex(request):
    if not request.is_ajax():
        return HttpResponse(status = 501)

    if request.method == 'GET':
        return _getIngredients()
    elif request.method == 'POST':
        data = json.loads(request.body)
        ingredient = _findIngredient(data)

        if ingredient:
            return _editIngredient(ingredient, data)
        else:
            return _addIngredient(data)

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

def _editIngredient(ingredient, data):
    try:
        ingredient.image = 'emptypath'
        ingredient.isSearchable = data['searchable']
        ingredient.save()
    except:
        return HttpResponse(status = 221)
    return HttpResponse(status = 200)

def _addIngredient(data):
    try:
        ingredient = Ingredient.objects.create(
            name = data['name'],
            image = 'emptypath',
            isSearchable = data['searchable'])
    except:
        return HttpResponse(status = 221)
    return HttpResponse(status = 200)

# unused method kept just in case
def deleteIngredient(request):
    if not request.is_ajax() or request.method != 'POST':
        return HttpResponse(status = 501)

    try:
        data = json.loads(request.body)
        ingredient = Ingredient.objects.get(name = data['name'])
        ingredient.delete()
    except DoesNotExist:
        HttpResponse(status = 220)
    except:
        return HttpResponse(status = 221)
    return HttpResponse(status = 200)

def topIngredients(request):
    if not request.is_ajax() or request.method != 'POST':
        return HttpResponse(status = 501)
