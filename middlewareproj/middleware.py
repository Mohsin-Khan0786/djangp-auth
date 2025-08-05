from django.utils.deprecation import MiddlewareMixin
import logging
from datetime import timedelta
from django.utils import timezone
from django.http import JsonResponse
from .models import BlockedIP
from core.models import RoleChoices 
logger = logging.getLogger('core.middleware')
 

class LoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')

        now = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info(f"[REQUEST] IP: {ip} at {now}")

    def process_response(self, request, response): 
        return response
     
    
class RateLimitMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        path = request.path


  
        if request.path.startswith('/admin/'):
            return None

        user = request.user
        now = timezone.now()
        limit = 20

        if user.is_authenticated and user.role != RoleChoices.GUEST:

            role_limits = {
                RoleChoices.GOLD: 10,
                RoleChoices.SILVER: 5,
                RoleChoices.BRONZE: 3,
            }
            limit = role_limits.get(user.role)

        try:
            blocked_ip = BlockedIP.objects.get(ip_address=ip)
            if now - blocked_ip.updated > timedelta(minutes=1):
                blocked_ip.count = 1
            
            else:
                blocked_ip.count += 1

            blocked_ip.save()
            print(limit)

            if blocked_ip.count >= limit:
                return JsonResponse(
                    {"error": f"Rate Limit Exceeded ({limit}/min). Try again after 1 minute."},
                    status=429
                )

        except BlockedIP.DoesNotExist:
            BlockedIP.objects.create(ip_address=ip, count=1)

        return None
