from django.contrib import admin

# Register your models here.
from .models import Pet

#this decorator registers our class object to the main admins list as an admin to the current apps
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
  #by creating the list the admins can see the objects data as the list 
  #defaultmethod given undem admin models 
  list_display= ['name','species','age','breed','sex']