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
        user=request.user
        if request.path .startswith('/admin/'):
            return None

        now = timezone.now()      
       
        try:
            # import pdb
            # pdb.set_trace()
            blocked_ip = BlockedIP.objects.get(ip_address=ip)
            if now - blocked_ip.updated > timedelta(minutes=1):
                blocked_ip.count = 1
            else:
                blocked_ip.count += 1

            blocked_ip.save()

            if blocked_ip.count >= 5:
                return JsonResponse(
                    {"error": "Rate Limit Exceeded.  Try again after 1 mins "},
                    status=429
                )
            else:
                return JsonResponse(
                    {"success": "HELOOOOOOOOOO"},
                    status=200
                )
        except BlockedIP.DoesNotExist:
            BlockedIP.objects.create(ip_address=ip)

        return None 