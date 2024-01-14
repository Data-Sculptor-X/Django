from django.contrib import admin

from .models import *

class EmailTemplateAdmin(admin.ModelAdmin):
	list_display= ('name','subject','created_at','updated_at')
admin.site.register(EmailTemplate,EmailTemplateAdmin)


class EmailNotificationAdmin(admin.ModelAdmin):
	list_display= ('username','name','subject','sended_at','notification','status')
admin.site.register(EmailNotification,EmailNotificationAdmin)
