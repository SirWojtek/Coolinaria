from django.db import models
from account.models import User
from ingredient.models import Ingredient


class RecipeManager(models.Manager):

    def create(self, name, author, formula):
        recipe = Recipe(name = name, author = author, formula = formula)
        recipe.save()
        return recipe

    def delete(self, recipeId):
        recipe = Recipe.objects.get(recipeId)
        for ingredient in recipe.getIngredients():
            ingredient.delete()
        recipe.delete()

class Recipe(models.Model):
    name = models.CharField(max_length = 64, unique = True)
    author = models.ForeignKey(User)
    lastUpdate = models.DateTimeField(auto_now = True)
    formula = models.TextField()

    objects = RecipeManager()

    def getIngredients(self):
        return Ingredients.objects.filter(recipe = self)

    def addIngredient(self, ingredient, quantity):
        ingredients = Ingredients(recipe = self, ingredient = ingredient, quantity = quantity)
        ingredients.save()


class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.CharField(max_length=10)