from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from django_otp.admin import OTPAdminSite
from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin


class OTPAdmin(OTPAdminSite):
    pass


admin_site = OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice, TOTPDeviceAdmin)

from django.contrib import admin
urlpatterns = [
    path('dadmin/', admin_site.urls),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL ,document_root = settings.STATIC_ROOT)