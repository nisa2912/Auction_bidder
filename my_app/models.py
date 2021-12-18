from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.



class Post(models.Model):
    Product_name = models.CharField(max_length=250)
    Product_description = models.TextField(null = True, blank = False)
    #Minimum_Bid_Price
    End_Time =models.DateTimeField(blank= False, null= True)
    #Product_Photo
    #Bidders


def __str__(self):
    return self.Product_name


class Bidding(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    #body =