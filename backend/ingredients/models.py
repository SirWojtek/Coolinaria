from django.db import models

#TODO: imagePath is not validated during creation of Ingredient model.
class IngredientManager(models.Manager):

    def create(self, name, description, imagePath, isSearchable = True):
        ingredient = Ingredient(name = name, description = description, image = imagePath,
                                isSearchable = isSearchable)

        ingredient.save()
        return ingredient


class Ingredient(models.Model):
    name = models.CharField(max_length = 64, unique = True)
    image = models.ImageField(upload_to = 'ingredient')
    isSearchable = models.BooleanField(default = True)
    objects = IngredientManager()
