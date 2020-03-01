from django.http import Http404, HttpResponseRedirect

from django.shortcuts import render

from .models import search

from django.urls import reverse

def index(request):
	print("Hello This is search page")
	return render(request, 'search/search.html')



