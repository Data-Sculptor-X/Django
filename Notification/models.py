from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class EmailTemplate(models.Model):
	name = models.CharField(max_length=255,null=True, blank=True)  
	subject = models.TextField(null=True, blank=True) 
	template = models.TextField(null=True, blank=True) 
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at= models.DateTimeField(auto_now=True)
	

class EmailNotification(models.Model):
	username = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True) 
	name =  models.ForeignKey(EmailTemplate,on_delete=models.SET_NULL, null=True, blank=True) 
	subject = models.TextField(null=True, blank=True) 
	template = models.TextField(null=True, blank=True) 
	sended_at = models.DateTimeField(auto_now_add=True)
	notification = models.BooleanField(default=False) 
	status = models.CharField(max_length=255,null=True, blank=True) 