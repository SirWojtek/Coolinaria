from recipe.models import Recipe, Ingredients
from ingredient.models import Ingredient
from account.models import User
from django.http import HttpResponse, JsonResponse
from django.db import DatabaseError
from django.core.exceptions import ObjectDoesNotExist
import json


def search(request):
    if not request.is_ajax() or request.method != 'POST':
        return HttpResponse(status=501)
    try:
        data = json.loads(request.body)
        recipes = Recipe.objects.search(data['ingredient'], data['type'])
        jsonRecipes = list()
        for recipe in recipes:
            jsonRecipes.append(recipe.getDict())
        return JsonResponse(jsonRecipes, safe=False)
    except KeyError:
        return HttpResponse(501)
    except (DatabaseError, ObjectDoesNotExist) as e:
        return JsonResponse(list())


def create(request):
    if not request.is_ajax() or request.method != 'POST' or not request.user:
        return HttpResponse(status=501)
    try:
        data = json.loads(request.body)
        recipe = Recipe.objects.create(name=data['name'],
                                       author=User.objects.get(username = data['author']),
                                       formula=data['formula'],
                                       duration=data['duration'],
                                       isAccepted=data['isAccepted'],
                                       difficulty=data['difficulty'])
        for ingredient in data['ingredients']:
            recipe.addIngredient(ingredient['name'], ingredient['amount'])
        for type in data['type']:
            recipe.addType(type)
    except KeyError:
        return HttpResponse(status=501)
    except (DatabaseError, ObjectDoesNotExist):
        return HttpResponse(status=220)
    return HttpResponse(status=200)


def update(request, recipeId):
    if not request.is_ajax() or request.method != 'POST' or not request.user:
        return HttpResponse(status=501)
    try:
        data = json.loads(request.body)
        recipe = Recipe.objects.get(id=recipeId)
        if not recipe.author.is_staff and recipe.author.name != request.user.name:
            return HttpResponse(status=501)
        recipe = Recipe.objects.update(recipeId=recipeId,
                                       name=data['name'],
                                       author=User.objects.get(username = data['author']),
                                       formula=data['formula'],
                                       duration=data['duration'],
                                       isAccepted=data['isAccepted'],
                                       difficulty=data['difficulty'])
        for ingredient in recipe.getIngredients():
            ingredient.delete()
        for ingredient in data['ingredients']:
            recipe.addIngredient(ingredient['name'], ingredient['amount'])
        for type in recipe.getTypes():
            type.delete()
        for type in data['type']:
            recipe.addType(type)
    except KeyError:
        return HttpResponse(status=501)
    except (DatabaseError, ObjectDoesNotExist):
        return HttpResponse(status=220)
    return HttpResponse(status=200)


def delete(request, recipeId):
    print 'REMOVING'
    if not request.user or not request.user.is_staff:
        return HttpResponse(status=501)
    print 'FUCK YEAH1'
    Recipe.objects.delete(recipeId)
    print 'FUCK YEAH2'
    return HttpResponse(status=200)