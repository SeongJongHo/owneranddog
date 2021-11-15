import json
from django.shortcuts import render
from django.views import View
from .models import Owner,Dog
from django.http import JsonResponse

class Owner_informationView(View):
  def post(self,request):
    data = json.loads(request.body)
    for owner_data in data:
      owner=Owner.objects.create(name=owner_data["owner_name"],age=owner_data["owner_age"]
      ,email=owner_data["email"])
    return JsonResponse(status=201)

class Dog_informationView(View):
  def post(self,request):
    data = json.loads(request.body)
    owner=Owner.objects.filter(name=data["owner_name"],email=data["owner_email"])
    for dog_data in data:
      dog=Dog.objects.create(name=dog_data["dog_name"],age=dog_data["dog_age"]
      ,owner=owner[0])
    return JsonResponse(status=201)
      


# Create your views here.
