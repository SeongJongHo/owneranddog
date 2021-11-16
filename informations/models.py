from django.db import models

class Owner(models.Model):
  id=models.AutoField(primary_key=True)
  name=models.CharField(max_length=45)
  email=models.EmailField(max_length=300)
  age=models.IntegerField(default=0)
    
  class Meta:
      db_table="owners"
  
  def __str__(self):
      return self.name

class Dog(models.Model):
  id=models.AutoField(primary_key=True)
  owner=models.ForeignKey("Owner",on_delete=models.CASCADE)
  name = models.CharField(max_length=45)
  age=models.IntegerField(default=0)
    
  class Meta:
      db_table="dogs"
    
  def __str__(self):
      return self.name
# Create your models here.
