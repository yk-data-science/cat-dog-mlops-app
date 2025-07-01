from django.urls import path
from .views import AddNumberAPIView

urlpatterns = [
    path('add-number/', AddNumberAPIView.as_view(), name='add-number'),
]