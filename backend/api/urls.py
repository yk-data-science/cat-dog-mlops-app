from django.urls import path
from .views import double, predict

urlpatterns = [
    path('double/', double, name='double'), # Only for test: Delete later
    path('predict/', predict, name='predict'),
]