from django.http import Http404, HttpResponseRedirect

from django.shortcuts import render

from .models import resume

from django.urls import reverse

def index(request):
	print("Hello This is resume page")
	return render(request, 'resume/resume.html')



