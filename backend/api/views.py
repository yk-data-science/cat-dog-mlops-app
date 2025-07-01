from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AddNumberAPIView(APIView):
    def post(self, request):
        number = request.data.get('number')
        if number is None:
            return Response({'error': 'No number provided'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            number = int(number)
        except ValueError:
            return Response({'error': 'Invalid number'}, status=status.HTTP_400_BAD_REQUEST)

        result = number + 10
        return Response({'result': result})
