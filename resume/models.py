from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class Resume(models.Model):
	first_name=models.CharField("First name", max_length=70, null=True)
	last_name=models.CharField("Last name", max_length=70, null=True)
	user_id=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	email=models.CharField("E-mail", max_length=50, null=True)
	phone=models.CharField("Phone", max_length=12, null=True)
	address=models.CharField("Address", max_length=200, null=True)
	city=models.CharField("City", max_length=40, null=True)
	state=models.CharField("State", max_length=40, null=True)
	country=models.CharField("Country", max_length=70, null=True)
	zip_code=models.CharField("Zip code", max_length=5, null=True)
	job_title=models.CharField("Job Title", max_length=100, null=True)
	summary=models.TextField("Summary", null=True)

class Education(models.Model):
	resume_id=models.ForeignKey(Resume, on_delete=models.CASCADE, null=True)
	organization_name=models.CharField("Organization", max_length=70, null=True)
	description=models.CharField("Description", max_length=70, null=True)
	title=models.CharField("Title", max_length=70, null=True)
	start_date=models.DateTimeField("Start date", null=True)
	end_date=models.DateTimeField("End date", null=True)


class Experience(models.Model):
	resume_id=models.ForeignKey(Resume, on_delete=models.CASCADE, null=True)
	position=models.CharField("Position", max_length=70, null=True)
	company_name=models.CharField("Organization", max_length=70, null=True)
	description=models.CharField("Description", max_length=70, null=True)
	start_date=models.DateTimeField("Start date", null=True)
	end_date=models.DateTimeField("End date", null=True)



