from django.db import models

#TODO: imagePath is not validated during creation of Ingredient model.
class IngredientManager(models.Manager):

    def create(self, name, image, isSearchable = True):
        ingredient = Ingredient(name = name, image = image,
                                isSearchable = isSearchable)

        ingredient.save()
        return ingredient


class Ingredient(models.Model):
    name = models.CharField(max_length = 64, unique = True)
    image = models.ImageField(upload_to = 'ingredient')
    isSearchable = models.BooleanField(default = True)
    objects = IngredientManager()

    def getDict(self):
        return {
            'name': self.name,
            'image': 'emptypath', # TODO: change to path
            'isSearchable' : self.isSearchable
        }
