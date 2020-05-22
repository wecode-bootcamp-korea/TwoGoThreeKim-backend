import json
import bcrypt
import jwt

from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Account


class SignUpView(View):
    def post(self, request):

        data = json.loads(request.body)

        try:
            if Account.objects.filter(email=data['email']).exists():
                return JsonResponse({'message':'EMAIL_ALREADY_EXISTS'},status=400)
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            Account.objects.create(
                        email = data['email'],
                        password = hashed_password,
                        name = data['name'],
                        nick_name = data['nick_name']
                )
            return JsonResponse({'message':'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message':'INVALID_KEYS'}, status=400)

class SignInView(View):
    def post(self, request):

        data = json.loads(request.body)

        try:
            if Account.objects.filter(email = data['email']).exists():
                if bcrypt.checkpw(data['password'].encode('utf-8'), Account.objects.get(email = data['email']).password.encode('utf-8')):
                    token = jwt.encode(
                            {'email':data['email']}, 'SECRET_KEY', algorithm='HS256').decode('utf-8')
                    return JsonResponse({'token':token},status=200)
                return JsonResponse({'message':'INVALID_USER'},status=401)
            return JsonResponse({'message':'INVALID_USER'},status=401)
        except KeyError:
            return JsonResponse({'message':'INVALID_KEYS'}, status=400)
