from django.urls import path
from .views import diabetes


urlpatterns = [
    path('diabetes/', diabetes, name="data")
]