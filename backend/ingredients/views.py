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

    
