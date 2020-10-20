from django.shortcuts import render
from .models import Job
# Create your views here.
def about_me(request):
 jobs = Job.objects.all()
 return    render(request,'aboutme.html',{'jobs':jobs})
