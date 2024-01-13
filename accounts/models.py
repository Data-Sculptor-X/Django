from django.db import models
from django.contrib.auth.models import User
# # Create your models here.


class UserProfile(models.Model):
	username = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True) 
	name = models.CharField(max_length=255, null=True,blank=True)  
	dob = models.DateField( null=True,blank=True)
	email = models.CharField(max_length=255, null=True,blank=True) 
	phone_no = models.CharField(max_length=255, null=True,blank=True) 
	profile_picture = models.ImageField( upload_to='userProfile/',null=True, blank=True) 
	secret_key = models.CharField(max_length=255, null=True,blank=True) 
	locked = models.CharField(max_length=255, null=True,blank=True) 
	active = models.BooleanField( null=True, blank=True) 
	tfa = models.BooleanField( null=True, blank=True)
	
# class OrganizationProfile(models.Model):
# 	username = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True) 
# 	name = models.CharField(max_length=255)  
# 	email = models.DateTimeField(auto_now_add=True)
# 	phone_no = models.DateTimeField(null=True, blank=True) 
# 	profile_picture = models.JSONField( null=True, blank=True) 
# 	secret_key = models.JSONField( null=True, blank=True) 
# 	locked = models.JSONField( null=True, blank=True) 
# 	active = models.JSONField( null=True, blank=True) 
	
class UserTrack(models.Model):
	username = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True) 
	refresh_token = models.CharField(max_length=255,null=True, blank=True)  
	login = models.DateTimeField(auto_now_add=True)
	logout = models.DateTimeField(null=True, blank=True) 
	remember_me= models.BooleanField(null=True, blank=True) 
	count = models.CharField(max_length=255,null=True, blank=True) 
	user_details = models.JSONField( null=True, blank=True) 