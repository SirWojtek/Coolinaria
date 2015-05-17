from recipe.models import Recipe
from ingredient.models import Ingredient
from account.models import User
from django.http import HttpResponse
from django.db import DatabaseError
import json

'''
This function could be executed only once, because of unique fields:
email for user
name for ingredient and recipe
'''
def index(request):
    user = User.objects.create(username = 'user', email='user@user.pl', password='user')
    ingredient = Ingredient.objects.create(name = 'kapusta', description = 'Zwyczajna, zielona',
                                           imagePath = 'ingredient/kapusta.jpg')
    recipe = Recipe.objects.create(name = 'Kapusta ala Hubert',
                           author = User.objects.get(email = 'user@user.pl'),
                           formula = 'Potnij na kwalki')
    recipe.addIngredient(ingredient, 14, 'kg')
    return HttpResponse('Hello, World!')


def create(request):
    if not request.is_ajax() or request.method != 'POST' or not request.User:
        return HttpResponse(status=501)
    try:
        data = json.loads(request.body)
        recipe = Recipe.objects.create(name=data['name'],
                                       author=User.objects.get(username = data['author']),
                                       formula=data['formula'])
        for ingredient in data['ingredients']:
            recipe.addIngredient(ingredient=Ingredient.objects.get(name=ingredient['name']),
                                 quantity=ingredient['quantity'])
    except KeyError:
        return HttpResponse(status=501)
    except DatabaseError:
        return HttpResponse(status=220)
    return HttpResponse(status=200)

def delete(request, recipeId):
    if not request.is_ajax() or request.method != 'POST' or not request.User or not request.User.is_staff:
        return HttpResponse(status=501)
    try:
        Recipe.objects.delete(id=recipeId)
    except DatabaseError:
        return HttpResponse(status=220)
    return HttpResponse(status=200)