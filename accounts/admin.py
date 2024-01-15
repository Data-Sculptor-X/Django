from django.contrib import admin
from .models import *
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
	list_display= ('username','name','email','phone_no','google_user','dx_user','mobile_verified','email_verified','tfa')

class UserTrackAdmin(admin.ModelAdmin):
	list_display= ('username','count','remember_me','login','logout')

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(UserTrack,UserTrackAdmin)