from django.db import models
from account.models import User
from ingredient.models import Ingredient


class RecipeManager(models.Manager):

    def create(self, name, author, formula):
        recipe = Recipe(name=name, author=author, formula=formula)
        recipe.save()
        return recipe

    def delete(self, recipeId):
        recipe = Recipe.objects.get(recipeId)
        for ingredient in recipe.getIngredients():
            ingredient.delete()
        recipe.delete()


class Difficulty:
    UNKNOWN = 'unknown'
    EASY = 'easy'
    NORMAL = 'normal'
    HARD = 'hard'

DIFFICULTY = (
    (Difficulty.UNKNOWN, 'Unknown'),
    (Difficulty.EASY, 'Easy'),
    (Difficulty.NORMAL, 'Normal'),
    (Difficulty.HARD, 'Hard')
)

class DishType:
    BREAKFAST = 'breakfast'
    DINNER = 'dinner'
    DESSERT = 'dessert'
    SUPPER = 'supper'
    SNACK = 'snack'

DISH_TYPE = (
    (DishType.BREAKFAST, 'Breakfast'),
    (DishType.DINNER, 'Dinner'),
    (DishType.DESSERT, 'Dessert'),
    (DishType.SUPPER, 'Supper'),
    (DishType.SNACK, 'Snack')
)

class Recipe(models.Model):
    name = models.CharField(max_length=64, unique=True)
    author = models.ForeignKey(User)
    lastUpdate = models.DateTimeField(auto_now = True)
    formula = models.TextField()
    duration = models.CharField(max_length = 100)
    displays = models.IntegerField(default=0)
    isAccepted = models.BooleanField(default=False)
    image = models.ImageField(upload_to='recipe')

    difficulty = models.CharField(max_length=7, choices=DIFFICULTY, default=Difficulty.UNKNOWN)

    objects = RecipeManager()

    def getIngredients(self):
        return Ingredients.objects.filter(recipe=self)

    def addIngredient(self, ingredientName, quantity):
        ingredients = self.getIngredients()
        for model in ingredients:
            if model.ingredient.name == ingredientName:
                return
        ingredients = Ingredients(recipe=self,
                                  ingredient=Ingredient.objects.get(name=ingredientName),
                                  quantity = quantity)
        ingredients.save()

    def getTypes(self):
        return Types.objects.filter(recipe = self)

    def addType(self, type):
        types = self.getTypes()
        for model in types:
            if model.type == type:
                return
        types = Types(recipe=self, type=type)
        types.save()


class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.CharField(max_length=100)


class Types(models.Model):
    recipe = models.ForeignKey(Recipe)
    type = models.CharField(max_length=10, choices=DISH_TYPE, default=DishType.BREAKFAST)