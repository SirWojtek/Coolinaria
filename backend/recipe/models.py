from django.db import models
from user.models import User
from ingredient.models import Ingredient


class RecipeManager(models.Manager):

    def create(self, name, author, formula):
        recipe = Recipe(name = name, author = author, formula = formula)
        recipe.save()
        return recipe


class Recipe(models.Model):
    name = models.CharField(max_length = 64, unique = True)
    author = models.ForeignKey(User)
    lastUpdate = models.DateTimeField(auto_now = True)
    formula = models.TextField()

    objects = RecipeManager()

    def getIngredients(self):
        return Ingredients.objects.filter(recipe = self)

    def addIngredient(self, ingredient, quantity, unit):
        ingredients = Ingredients(recipe = self, ingredient = ingredient, quantity = quantity,
                                  unit = unit)
        ingredients.save()


class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10)