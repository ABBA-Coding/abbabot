import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .functions import send_message


@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        # Handle incoming webhook request
        data = json.loads(request.body)
        user_id = data['message']['from']['id']
        send_message(user_id)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)
