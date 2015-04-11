from recipe.models import Recipe
from ingredient.models import Ingredient
from django.contrib.auth.models import User
from django.http import HttpResponse

'''
This function could be executed only once, because of unique fields:
email for user
name for ingredient and recipe
'''
def index(request):
    user = User.objects.create_user(username = 'hubert', email='hubert@hubert.pl', password='hubert')
    user.save()  # TODO: implement user model with auto save (like ingredient and recipe)
    ingredient = Ingredient.objects.create(name = 'kapusta')
    recipe = Recipe.objects.create(name = 'Kapusta ala Hubert',
                           author = User.objects.get(email = 'hubert@hubert.pl'),
                           formula = 'Potnij na kwalki')
    recipe.addIngredient(ingredient, 14, 'kg')
    return HttpResponse('Hello, World!')
