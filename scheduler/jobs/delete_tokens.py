from django.utils import timezone
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken,BlacklistedToken
from datetime import timedelta

def delete_tokens():
    current_time = timezone.now()
    OutstandingToken.objects.filter(expires_at__lt=current_time).delete()
    BlacklistedToken.objects.filter(expires_at__lt=current_time).delete()