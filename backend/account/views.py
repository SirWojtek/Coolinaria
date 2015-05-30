from account.models import User
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib.auth import logout as userLogout, login as userLogin
from django.db import DatabaseError
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    if request.method != 'POST':
        return HttpResponse(status=501)
    try:
        data = json.loads(request.body)
        user = User.objects.authenticate(email=data['email'], password=data['password'])
        userLogin(request, user)
        print 'Login: ' + str(user)
    except KeyError:
        return HttpResponse(status=501)
    except (ValidationError, DatabaseError, ObjectDoesNotExist):
        return HttpResponse(status=220)
    return JsonResponse({'isModerator': True})

def logout(request):
    print 'Logout: ' + str(request.user)
    userLogout(request)
    return HttpResponse(status=200)

@csrf_exempt
def account(request):
    if request.method != 'POST':
        return HttpResponse(status=501)
    try:
        data = json.loads(request.body)
        if request.user.is_anonymous():
            createOrThrow(data)
        else:
            user = User.objects.update(userId=request.user.id,
                                       email=data['email'],
                                       password=data['password'])
            request.user = user
            print 'Update: ' + str(user)
    except (KeyError, ObjectDoesNotExist):
        return HttpResponse(status=501)
    except DatabaseError:
        return HttpResponse(status=220)
    except ValidationError:
        return HttpResponse(status=221)
    return HttpResponse(status=200)

def createOrThrow(data):
    try:
        User.objects.get(email=data['email'])
    except ObjectDoesNotExist:
        user = User.objects.create(email=data['email'],
            password=data['password'])
        print 'Create: ' + str(user)
        return
    raise ObjectDoesNotExist

