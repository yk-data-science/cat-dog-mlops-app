from django.shortcuts import render

import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view

from ml_model.train_model import predict_image

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


@csrf_exempt
# def predict(request):
#     if request.method != "POST":
#         return JsonResponse({"error": "POST method required"}, status=405)

#     if 'file' not in request.FILES:
#         return JsonResponse({"error": "No file uploaded"}, status=400)

#     try:
#         img_file = request.FILES['file']
#         prediction = predict_image(img_file) # Use the predict_image function from train_model.py
#         if prediction is None:
#             return JsonResponse({"error": "Prediction failed"}, status=500)
#         return JsonResponse({"prediction": prediction})
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=500)

# Using DRF APIView for better structure
@api_view(['POST'])
def predict(request):
    file = request.FILES.get('file')
    if not file:
        return Response({'error': 'No file uploaded'}, status=400)

    result = predict_image(file)
    return Response(result)