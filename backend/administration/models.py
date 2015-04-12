from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager


class UserManager(UserManager):

    def create(self, username, email, password):
        user = User(username = username, email = email, password = password)
        user.save()
        return user


class User(AbstractUser):
    objects = UserManager()
