from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import auth
from django.template.context_processors import csrf
#from quotes.quotes import Quotes
from . import quotes

def index(request):
	print("Hello This is main page")
	return render(request, 'resume\main.html', {'quote': quotes.get_random_quote()})


def login(request):
	args={}
	args.update(csrf(request))
	args['quote']=quotes.get_random_quote()
	if request.POST:
		username=request.POST.get('username', '')
		password=request.POST.get('password', '')
		user=auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return render(request, 'resume\main.html', args)	
		else:
			args['login_error']="user not found"
			print("error")
			return render(request, 'login.html', {'error': 'Wrong password or username'})
	else:
		return render(request, 'login.html', args)		
	#return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	return render(request, 'resume\main.html')	

def signup(request):
	args={}
	args.update(csrf(request))
	if request.POST:
		username=request.POST.get('new_username', '')
		password=request.POST.get('new_password', '')
		passwordcheck=request.POST.get('passwordcheck', '')
		email=request.POST.get('email', '')
		first_name=request.POST.get('first_name', '')
		last_name=request.POST.get('last_name', '')
		if (password != passwordcheck):
			return render(request, 'signup.html', {'error': "Passwords don't match"})
		user = User.objects.create_user(username, email, password)
		if user:
			user.first_name=first_name
			user.last_name=last_name
			user.save()
			return render(request, 'login.html', args)
		else:
			return render(request, 'signup.html', {'error': "Something went wrong!"})
	else:
		return render(request, 'signup.html')	


def automation(request):
	return render(request, 'automation.html', {'quote': quotes.get_random_quote()})

def myresume(request):
	return render(request, 'myresume.html')


