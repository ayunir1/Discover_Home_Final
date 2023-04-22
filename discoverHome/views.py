from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from django.core import serializers
from django.http import HttpResponse
from .models import UserInfo
import json

def home(request):
    email = 'email' in request.session
    if email:
        return render(request, "registration/home.html", {"mail": request.session['email']})
    else:
        return render(request, "registration/home.html", {"mail": ""})
# Create your views here.
def login(request):
    return render(request, "registration/login.html")
def profile(request):
    email = 'email' in request.session
    if email:
        return render(request, "registration/profile.html", {"mail": request.session['email']})
    else:
        return render(request, "registration/profile.html", {"mail": ""})
def logout(request):
    del request.session['email']
    return redirect("/")
def signup(request):
    return render(request,"registration/signUp.html")
def register(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            
            foo_instance = UserInfo.objects.create(username = data['name'], email = data['email'], password = data['pwd'])
            
            return JsonResponse(data)
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')
    # some error occured
    return JsonResponse({"error": ""}, status=400)

def signin(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            infodata = data = json.load(request)
            data = UserInfo.objects.raw('SELECT * FROM user WHERE  email = %s and password = %s', (infodata['email'],infodata['pwd'],))
            
            if data:
                request.session['email'] = infodata['email']
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'failed'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')
    # some error occured
    return JsonResponse({"error": ""}, status=400)

def updateprofile(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            infodata = data = json.load(request)
            print(infodata['name'])
            print(infodata['pwd'])
            data = UserInfo.objects.get(email=request.session['email'])
            data.username = infodata['name']
            data.password = infodata['pwd']
            data.save()
            
            if data:
                # request.session['email'] = infodata['email']
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'failed'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')
    # some error occured
    return JsonResponse({"error": ""}, status=400)

def profile_home(request) :
    return render(request, 'profile_home.html', {})

def concert(request) :
    return render(request, 'concert.html', {})

    