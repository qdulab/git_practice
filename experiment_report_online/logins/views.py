# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
	return HttpResponse("Hello world!")

def user_login(request):
	return render_to_response('logins/login.html')
