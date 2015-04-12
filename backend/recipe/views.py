from recipe.models import Recipe
from ingredient.models import Ingredient
from administration.models import User
from django.http import HttpResponse


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
