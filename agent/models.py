from django.db import models
from policyBaazar.models import UserProfile

# Create your models here.
class Main_Category(models.Model):
    catname = models.CharField(max_length=50)
    catdesc = models.CharField(max_length=200)
    cat_image = models.ImageField(upload_to="cat_image/", blank=True)
    creation_date = models.DateTimeField(auto_now=True)
   

class Main_SubCategory(models.Model):
    catid = models.ForeignKey(Main_Category, on_delete=models.CASCADE)
    sub_catname = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now=True)

class Insurance_Policy(models.Model):
    catid = models.ForeignKey(Main_Category, on_delete=models.CASCADE)
    sub_id = models.ForeignKey(Main_SubCategory, on_delete=models.CASCADE)
    policy_name = models.CharField(max_length=100)
    sum_assured = models.IntegerField()
    premium = models.IntegerField()
    tenure = models.IntegerField()
    creation_date = models.DateTimeField(auto_now=True)