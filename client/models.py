from policyBaazar.models import UserProfile
from django.contrib.auth.models import User
from agent.models import Insurance_Policy
from django.db import models
from policyBaazar.models import UserProfile


# Create your models here.
class home_details(models.Model):
    #policy_holder = models.OneToOneField(policy_holder, on_delete=models.CASCADE)
    add_line1 = models.CharField(max_length=100)
    add_line2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()
    area = models.IntegerField()
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class vehicle_details(models.Model):
    registration_no = models.CharField(max_length=100)
    chassis_no = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    year = models.IntegerField()
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class travel_details(models.Model):
    travelling_to = models.CharField(max_length=100)
    start_Date = models.CharField(max_length=50)
    End_Date = models.CharField(max_length=50)
    passengers = models.IntegerField()
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class health_details(models.Model):
    name = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    current_doctor = models.CharField(max_length=100)
    date_visit = models.CharField(max_length=50)
    occupation = models.CharField(max_length=100)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class life_details(models.Model):
    name = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    health_issue = models.CharField(max_length=100)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class mobile_details(models.Model):
    company_name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    purchasing_date = models.CharField(max_length=50)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class policy_holder(models.Model):
    # policy_holder_name = models.CharField(max_length=50)
    # email = models.EmailField(max_length=50)
    # mobile = models.IntegerField()
    policy_id = models.ForeignKey(Insurance_Policy, on_delete=models.CASCADE)
    placedby = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    policy_date = models.DateField(auto_now=True)