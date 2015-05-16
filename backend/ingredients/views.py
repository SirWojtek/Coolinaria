from django.http import HttpResponse
from ingredients.models import Ingredient
import json

def getIngredients(request):
    if not request.is_ajax() or request.method != 'GET' or not request.User:
        return HttpResponse(status = 501)

    ingredients = list(Ingredient.objects.all())
    return HttpResponse(json.dumps(ingredients),
        content_type = "application/json", status = 200)

def addIngredient(request):
    if not request.is_ajax() or request.method != 'POST' or not request.User:
        return HttpResponse(status = 501)

    try:
        data = json.loads(request.body)
        ingredient = Ingredient.objects.create(
            name = data['name'],
            description = data['description'],
            image = 'emptypath',
            isSearchable = data['searchable'])
    except:
        return HttpResponse(status = 221)
    return HttpResponse(status = 200)

def editIngredient(request):
    if not request.is_ajax() or request.method != 'POST' or not request.User:
        return HttpResponse(status = 501)

    try:
        data = json.loads(request.body)
        ingredient = Ingredient.objects.filter(name = data['name'])
        if not ingredient:
            return HttpResponse(status = 220)
        ingredient.description = data['description']
        ingredient.image = 'emptypath'
        ingredient.isSearchable = data['searchable']
        ingredient.save()
    except:
        return HttpResponse(status = 501)
    return HttpResponse(status = 200)


