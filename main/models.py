from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    type = models.CharField(max_length = 255)
    date_added =  models.DateField(auto_now_add=True, name="date_added")
    user = models.ForeignKey(User, on_delete=models.CASCADE)