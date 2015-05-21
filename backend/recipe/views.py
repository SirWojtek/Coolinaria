from recipe.models import Recipe, Ingredients
from recipe.forms import RecipeForm
from ingredient.models import Ingredient
from account.models import User
from django.http import HttpResponse, JsonResponse
from django.db import DatabaseError
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def search(request):
    if request.method != 'POST':
        return HttpResponse(status=501)
    try:
        data = json.loads(request.body)
        recipes = _searchForRecipe(data)
        jsonRecipes = list()
        for recipe in recipes:
            jsonRecipes.append(recipe.getDict())
        return JsonResponse(jsonRecipes, safe=False)
    except KeyError:
        return HttpResponse(status = 501)
    except (DatabaseError, ObjectDoesNotExist) as e:
        return HttpResponse(json.dumps([]))

def _searchForRecipe(data):
    ingredient = data.get('ingredient')
    recipeType = data.get('type')

    if ingredient and recipeType:
        Ingredient.objects.get(name=ingredient).increaseDisplays()
        return Recipe.objects.search(ingredient, recipeType)
    elif ingredient:
        Ingredient.objects.get(name=ingredient).increaseDisplays()
        return Recipe.objects.searchIngredientName(ingredient)
    elif recipeType:
        return Recipe.objects.searchType(recipeType)
    
    raise KeyError

def getId(request, id):
    if request.method != 'GET':
        return HttpResponse(status=501)

    try:
        recipe = Recipe.objects.get(id = id)
        return HttpResponse(json.dumps(recipe.getDict()))
    except:
        return HttpResponse(status = 502)

# def index(request):
#     recipe = Recipe.objects.create(name="Jajka w sosie z Twojego starego",
#         author=User.objects.get(username = 'admin@admin.pl'),
#                                    formula='Pokoroic w plastry',
#                                    duration='W chuj',
#                                    isAccepted=True,
#                                    difficulty='easy')
#     for ingredient in [{'name':'Ziemniaki', 'amount':'w pizdu'}, 
#                        {'name':'Jajka', 'amount':'strasznie duzo'}]:
#         recipe.addIngredient(ingredient['name'], ingredient['amount'])
#     for type in ['breakfast', 'dinner']:
#         recipe.addType(type)

@csrf_exempt
def create(request):
    if request.method != 'POST' or not request.user:
        return HttpResponse(status=501)
    try:
        data = json.loads(request.POST['recipe'])
        recipe = Recipe.objects.create(name=data['name'],
                                       author=User.objects.get(username = data['author']),
                                       formula=data['formula'],
                                       duration=data['duration'],
                                       image=request.FILES.itervalues().next(),
                                       difficulty=data['difficulty'])
        for ingredient in data['ingredients']:
            recipe.addIngredient(ingredient['name'], ingredient['amount'])
        for type in data['type']:
            recipe.addType(type)
    except KeyError:
        return HttpResponse(status=501)
    # except (DatabaseError, ObjectDoesNotExist):
    #     return HttpResponse(status=220)
    return HttpResponse(status=200)


def update(request, recipeId):
    if request.method != 'POST' or not request.user:
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
    if not request.user or not request.user.is_staff:
        return HttpResponse(status=501)
    Recipe.objects.delete(recipeId)
    return HttpResponse(status=200)
