from django.urls import path

from . import views

app_name='resume'

urlpatterns = [
	path('', views.index, name = 'index'),
	path('addnew/', views.addnew, name = 'addnew'),
	path('<int:resume_id>/', views.resume_details, name='resume_details'),
	path('<int:resume_id>/edit/', views.editresume, name="editresume"),
	path('<int:resume_id>/delete/', views.deleteresume, name="deleteresume")	
	#path('<int:article_id>/', views.detail, name='detail'),
	#path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment')	
]