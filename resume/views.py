from django.http import Http404, HttpResponseRedirect
from django.template.context_processors import csrf
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Resume, Education, Experience
from django.utils import timezone
from JobMarket import quotes
from django.urls import reverse, NoReverseMatch

def index(request):
	print("Hello This is resume page")
	print(request.user.id)
	resumes_list=Resume.objects.filter(user_id=request.user.id)
	return render(request, 'resume/resume.html', {'resumes_list': resumes_list, 'quote': quotes.get_random_quote()})

def addnew(request):
	args={}
	args.update(csrf(request))
	args['quote']=quotes.get_random_quote()
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

#### Education
		start_dates=request.POST.getlist('year_start', '')
		end_dates=request.POST.getlist('year_end', '')
		organizations=request.POST.getlist('organization', '')
		titles=request.POST.getlist('title', '')
		descriptions=request.POST.getlist('description', '')
		ed_list=[]
		for i in range(len(start_dates)):
			if start_dates[i]!="" and end_dates[i]!="" and organizations[i]!="" and titles[i]!="":
				ed=Education(start_date=start_dates[i], 
					end_date=end_dates[i], 
					organization_name=organizations[i], 
					title=titles[i], 
					description=descriptions[i], 
					resume_id=r)
				ed_list.append(ed)
#### Experience		
		ex_start_dates=request.POST.getlist('ex_year_start', '')
		ex_end_dates=request.POST.getlist('ex_year_end', '')
		companies=request.POST.getlist('company', '')
		positions=request.POST.getlist('position', '')
		ex_descriptions=request.POST.getlist('ex_description', '')
		ex_list=[]
		for i in range(len(ex_start_dates)):
			if ex_start_dates[i]!="" and ex_end_dates[i]!="" and companies[i]!="" and positions[i]!="":
				ex=Experience(start_date=ex_start_dates[i], 
						end_date=ex_end_dates[i], 
						company_name=companies[i], 
						position=positions[i], 
						description=ex_descriptions[i], 
						resume_id=r)
				ex_list.append(ex)

		try:
			r.save()
			for x in ed_list:
				x.resume_id=r
				x.save()
			for y in ex_list:
				y.resume_id=r
				y.save()	
			return render(request, 'resume/addnew.html', {'status': 'Resume was added', 'quote': quotes.get_random_quote()})
		except:
			return render(request, 'resume/addnew.html', {'error': 'Something went wrong', 'quote': quotes.get_random_quote()})			

	else:
		return render(request, 'resume/addnew.html', args)


def resume_details(request, resume_id):
	if request.user == Resume.objects.get(id=resume_id).user_id:
		safety=True;
	else:
		safety=False;		
	resume=Resume.objects.get(id=resume_id)
	experience=Experience.objects.filter(resume_id=resume_id)
	education=Education.objects.filter(resume_id=resume_id)
	return render(request, 'resume/resume_details.html', {'resume': resume, 'experience': experience, 'education': education, 'safety': safety, 'quote': quotes.get_random_quote()})


def editresume(request, resume_id):
	args={}
	args.update(csrf(request))
	args['quote']=quotes.get_random_quote()
	if request.user != Resume.objects.get(id=resume_id).user_id:
		return render(request, 'resume/addnew.html', {'error': 'You don\'t have permission edit this page', 'quote': quotes.get_random_quote()})	
	if request.POST.get('job_title', ''):
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
		
		r=Resume(id=resume_id,
				first_name=first_name,
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

#### Education
		start_dates=request.POST.getlist('year_start', '')
		end_dates=request.POST.getlist('year_end', '')
		organizations=request.POST.getlist('organization', '')
		titles=request.POST.getlist('title', '')
		descriptions=request.POST.getlist('description', '')
		ed_list=[]
		for i in range(len(start_dates)):
			if start_dates[i]!="" and end_dates[i]!="" and organizations[i]!="" and titles[i]!="":
				ed=Education(start_date=start_dates[i], 
					end_date=end_dates[i], 
					organization_name=organizations[i], 
					title=titles[i], 
					description=descriptions[i], 
					resume_id=r)
				ed_list.append(ed)
#### Experience		
		ex_start_dates=request.POST.getlist('ex_year_start', '')
		ex_end_dates=request.POST.getlist('ex_year_end', '')
		companies=request.POST.getlist('company', '')
		positions=request.POST.getlist('position', '')
		ex_descriptions=request.POST.getlist('ex_description', '')
		ex_list=[]
		for i in range(len(ex_start_dates)):
			if ex_start_dates[i]!="" and ex_end_dates[i]!="" and companies[i]!="" and positions[i]!="":
				ex=Experience(start_date=ex_start_dates[i], 
						end_date=ex_end_dates[i], 
						company_name=companies[i], 
						position=positions[i], 
						description=ex_descriptions[i], 
						resume_id=r)
				ex_list.append(ex)

		try:
			r.save()
			Experience.objects.filter(resume_id=resume_id).delete()
			Education.objects.filter(resume_id=resume_id).delete()
			for x in ed_list:
				x.save()
			for y in ex_list:
				y.save()	
			return render(request, 'resume/edit.html', {'status': 'Resume was edited', 'quote': quotes.get_random_quote()})
		except:
			return render(request, 'resume/edit.html', {'error': 'Something went wrong', 'quote': quotes.get_random_quote()})			

	else:
		resume=Resume.objects.get(id=resume_id)
		experience=Experience.objects.filter(resume_id=resume_id)
		education=Education.objects.filter(resume_id=resume_id)
		return render(request, 'resume/edit.html', {'resume': resume, 'experience': experience, 'education': education, 'quote': quotes.get_random_quote()})


def deleteresume(request, resume_id):
	resume=Resume.objects.get(id=resume_id)
	try: 
		resume.delete()
		return render(request, 'resume/delete.html', {'status': 'Resume was deleted', 'quote': quotes.get_random_quote()})
	except:
		return render(request, 'resume/delete.html', {'error': 'Something went wrong', 'quote': quotes.get_random_quote()})	
	
