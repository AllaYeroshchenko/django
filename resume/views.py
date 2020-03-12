from django.http import Http404, HttpResponseRedirect
from django.template.context_processors import csrf
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Resume, Education
from django.utils import timezone

from django.urls import reverse

def index(request):
	print("Hello This is resume page")
	return render(request, 'resume/resume.html')

def addnew(request):
	args={}
	args.update(csrf(request))
	if request.POST:
		first_name=request.POST.get('first_name', '')
		last_name=request.POST.get('last_name', '')
		email=request.POST.get('email', '')
		phone=request.POST.get('phone', '')
		address=request.POST.get('address', '')
		city=request.POST.get('city', '')
		state=request.POST.get('state', '')
		country=request.POST.get('country', '')
		zip_code=request.POST.get('zip_code', '')
		job_title=request.POST.get('job_title', '')
		summary=request.POST.get('summary', '')
		
		r=Resume(first_name=first_name,
				last_name=last_name,
				email=email,
				phone=phone,
				address=address,
				city=city,
				state=state,
				country=country,
				zip_code=zip_code,
				summary=summary,
				job_title=job_title,
				user_id=request.user)

		start_dates=request.POST.getlist('year_start', '')
		end_dates=request.POST.getlist('year_end', '')
		organizations=request.POST.getlist('organization', '')
		ed_list=[]
		for i in range(len(start_dates)):
			ed=Education(start_date=start_dates[i], 
					end_date=end_dates[i], 
					organization_name=organizations[i], 
					title="", 
					description="", 
					resume_id=r)
			ed_list.append(ed)

		try:
			r.save()
			for x in ed_list:
				x.save()
			return render(request, 'resume/addnew.html', {'status': 'Resume was added'})
		except:
			render(request, 'resume/addnew.html', {'error': 'Something went wrong'})			

	else:
		return render(request, 'resume/addnew.html', args)

