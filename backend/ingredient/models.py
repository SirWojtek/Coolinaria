from django.db import models

class IngredientManager(models.Manager):

    def create(self, name):
        ingredient = Ingredient(name = name)
        ingredient.save()
        return ingredient


class Ingredient(models.Model):
    name = models.CharField(max_length = 64, unique = True)
    objects = IngredientManager()
