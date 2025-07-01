# backend/backend/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Csrf_exempt allows POST requests without CSRF token
def double(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            number = data.get('number', None)
            if number is None:
                return JsonResponse({'error': 'number is required'}, status=400)
            result = number * 2
            return JsonResponse({'result': result})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'POST method required'}, status=405)
