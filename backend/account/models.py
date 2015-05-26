from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class UserManager(UserManager):

    def create(self, email, password):
        validate_email(email)
        user = User.objects.create_user(username=email, email=email, password=password)
        user.is_staff = False
	user.save()
        return user

    def authenticate(self, email, password):
        validate_email(email)
        user = User.objects.get(username=email)
        print user
        user = authenticate(username=user.username, password=password)
        print user
        if user is None or not user.is_active:
            raise(ValidationError('User authentication failed!'))
        return user

    def update(self, userId, email, password):
        validate_email(email)
        user = User.objects.get(id=userId)
        user.username = email
        user.email = email
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    objects = UserManager()
