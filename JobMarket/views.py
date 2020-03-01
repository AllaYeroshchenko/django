from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib import auth
from django.template.context_processors import csrf


def index(request):
	print("Hello This is main page")
	return render(request, 'resume\main.html')


def login(request):
	args={}
	args.update(csrf(request))
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
	return render(request, 'resume\\main.html')	