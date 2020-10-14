from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,request,Http404
from .models import Pet
def home(request):
    pets =Pet.objects.all()

    return render(request,'home.html',{'pets':pets})

def pet_details(request,pet_id):
   try:
    pet = Pet.objects.get(id=pet_id)
    return render(request,'pet_detail.html',{'pet':pet})
   except Pet.DoesNotExist:
       raise Http404("requested object doest not exist")