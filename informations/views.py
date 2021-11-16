import json
from django.http import JsonResponse
from django.views import View
from .models import Owner,Dog

class Owner_informationView(View):
  
  def post(self,request):
    data = json.loads(request.body)
    Owner.objects.create(
      name=data["owner_name"],
      age=data["owner_age"],
      email=data["email"])

    return JsonResponse({'MESSAGE':'CREATED'}, status=201)

  def get(self,request):
   
    owners=Owner.objects.all()
    results=[]
    for owner in owners:
        dog=owner.dog_set.values("name","age").filter(owner=owner.id)
        results.append({
        "dogs":[d for d in dog],
        # dog_set = Dog.objects
        # "dogs" : list(owner.dog_set.values('name',"age")),
        "owner_name" : owner.name,
        "owner_age" : owner.age,
        "email" : owner.email,
        
        })
    return JsonResponse({"result":results}, status=200)

class Dog_informationView(View):
  
  def post(self,request):
 
    data = json.loads(request.body)
    owner=Owner.objects.filter(name=data["owner_name"],email=data["email"])
    
    Dog.objects.create(name=data["dog_name"],age=data["dog_age"],owner=owner[0])
   
    return JsonResponse({'MESSAGE':'CREATED'}, status=201)
  
  def get(self,request):

    dogs=Dog.objects.all()
    results=[]
    for dog in dogs:
						results.append(
							{
									"dog_name" : dog.name,
                  "dog_age" : dog.age,
                  "owner":dog.owner.name
                  
							}
				)
    return JsonResponse({"result":results}, status=200)
    


# Create your views here.
