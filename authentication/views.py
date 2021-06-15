from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
import json
from django.http import JsonResponse

# Create your views here.

class UsernameValidationView(View):
    def post(self, request):
        data= json.load(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'usernaem_error':'InValid Username'})
        if User.objects.filter(username=username).exists():
            return JsonResponse({'usernaem_error':'Username Already Taken'})            
        return JsonResponse({'username-valid': True})    

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')