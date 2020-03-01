from django.http import Http404, HttpResponseRedirect

from django.shortcuts import render

from .models import statistic

from django.urls import reverse

def index(request):
	print("Hello This is statistic page")
	return render(request, 'statistic/statistic.html')



