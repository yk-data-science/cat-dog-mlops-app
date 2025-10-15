from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

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

def predict(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST method required"}, status=405)

    # check if file is in request
    uploaded_file = request.FILES.get("file")
    if not uploaded_file:
        return JsonResponse({"error": "file is required"}, status=400)

    # save the uploaded file to a temporary location
    # path = default_storage.save(uploaded_file.name, ContentFile(uploaded_file.read()))

    # img = Image.open(path)
    # result = model.predict(img)
    
    result = "cat" # Dummy result
    return JsonResponse({"result": result})
