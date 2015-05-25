from recipe.models import Recipe, Ingredients, DISH_TYPE
from ingredient.models import Ingredient
from account.models import User
from django.http import HttpResponse, JsonResponse
from django.db import DatabaseError
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
import json
import xml.etree.ElementTree as ET
import random

f = 'przepisy2.xml'

def load(request):
    tree = ET.parse(f)
    root = tree.getroot()

    for przepis in root:
        nazwa = przepis[0].text
        fota = przepis[1].text
        czas = przepis[2].text
        ocena = przepis[3].text
        kroki = ""
        skladniki = []

        for krok in przepis[4]:
            kroki += krok.text + r'\n'
        for skladnik in przepis[5]:
            skladniki.append(skladnik)

        recipe = Recipe.objects.create(name=nazwa,
                                       author=User.objects.get(username = 'admin@admin.pl'),
                                       formula=kroki,
                                       duration=czas,
                                       image='null',
                                       difficulty=ocena)
        recipe.image.name = 'recipe/' + fota
        for skladnik in skladniki:
            recipe.addIngredient(skladnik[0], skladnik[1])
        recipe.addType(DISH_TYPE[random.randint(0, 4)][1])
        print recipe
    return HttpResponse()

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
    except (DatabaseError, ObjectDoesNotExist):
        return HttpResponse(status=220)
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

def toAccept(request):
    try:
        recipes = []
        for recipe in Recipe.objects.filter(isAccepted = False):
            recipes.append(recipe.getDict())
        return HttpResponse(json.dumps(recipes))
    except:
        return HttpResponse(status = 502)
