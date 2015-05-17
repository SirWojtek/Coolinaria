from django.db import models
from account.models import User
from ingredient.models import Ingredient


class RecipeManager(models.Manager):

    def create(self, name, author, formula, duration, isAccepted, difficulty):
        recipe = Recipe(name=name, author=author, formula=formula, duration=duration,
                        isAccepted=isAccepted, difficulty=difficulty)
        recipe.save()
        return recipe

    def update(self, recipeId, name, author, formula, duration, isAccepted, difficulty):
        recipe = Recipe.objects.get(id=recipeId)
        recipe.name = name
        recipe.author = author
        recipe.formula = formula
        recipe.duration = duration
        recipe.isAccepted = isAccepted
        recipe.difficulty = difficulty
        recipe.save()
        return recipe

    def delete(self, recipeId):
        recipe = Recipe.objects.get(id=recipeId)
        for ingredient in recipe.getIngredients():
            ingredient.delete()
        for type in recipe.getTypes():
            type.delete()
        recipe.delete()

    def search(self, ingredientName, typesToSearch):
        searchRecipes = list()
        ingredient = Ingredient.objects.get(name=ingredientName)
        for value in Ingredients.objects.filter(ingredient=ingredient):
            currentTypes = value.recipe.getTypes(jsonFormat=True)
            for type in typesToSearch:
                if type in currentTypes:
                    searchRecipes.append(value.recipe)
                    break
        return searchRecipes


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
    name = models.CharField(max_length=150, unique=True)
    author = models.ForeignKey(User)
    lastUpdate = models.DateTimeField(auto_now = True)
    formula = models.TextField()
    duration = models.CharField(max_length = 100)
    displays = models.IntegerField(default=0)
    isAccepted = models.BooleanField(default=False)
    image = models.ImageField(upload_to='recipe', blank=True)
    difficulty = models.CharField(max_length=7, choices=DIFFICULTY, default=Difficulty.UNKNOWN)

    objects = RecipeManager()

    def getDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.getTypes(jsonFormat=True),
            'author': self.author.username,
            'ingerdients': self.getIngredients(jsonFormat=True),
            'formula': self.formula,
            'duration': self.duration,
            'dispalys': self.displays,
            'isAccepted': self.isAccepted,
            'difficulty': self.difficulty,
            'lastUpdate': self.lastUpdate.isoformat(),
            'image': 'emptypath' # TODO: change to path
        }

    def getIngredients(self, jsonFormat=False):
        jsonIngredients = list()
        ingredients = Ingredients.objects.filter(recipe=self)
        if not jsonFormat:
            return ingredients
        for ingredient in ingredients:
            jsonIngredients.append({'name': ingredient.ingredient.name, 'amount': ingredient.quantity})
        return jsonIngredients

    def addIngredient(self, ingredientName, quantity):
        ingredients = self.getIngredients()
        for model in ingredients:
            if model.ingredient.name == ingredientName:
                if model.quantity == quantity:
                    return
                else:
                    model.quantity = quantity
                    model.save()
                    return
        ingredients = Ingredients(recipe=self,
                                  ingredient=Ingredient.objects.get(name=ingredientName),
                                  quantity = quantity)
        ingredients.save()

    def getTypes(self, jsonFormat=False):
        jsonTypes = list()
        types = Types.objects.filter(recipe = self)
        if not jsonFormat:
            return types
        for type in types:
            jsonTypes.append(str(type.type))
        return jsonTypes

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