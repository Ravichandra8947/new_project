from django.urls import path
from .views import AddAPIView

urlpatterns = [
    path('add/', AddAPIView.as_view(), name='add-list-create'),
]
