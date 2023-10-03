from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField(default=1)  
    description = models.TextField()
    price = models.IntegerField()
    date_added =  models.DateField(auto_now_add=True, name="date_added")
    image_url= models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)