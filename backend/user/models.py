from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class UserManager(UserManager):

    def create(self, username, email, password):
        validate_email(email)
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return user

    def authenticate(self, email, password):
        validate_email(email)
        user = User.objects.get(email=email)
        print user
        user = authenticate(username=user.username, password=password)
        print user
        if user is None or not user.is_active:
            raise(ValidationError('User authentication failed!'))
        return user

    def update(self, userId, username, email, password):
        validate_email(email)
        user = User.objects.get(id=userId)
        if user is None:
            raise KeyError('Wrong user ID')
        user.username = username
        user.email = email
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    objects = UserManager()
