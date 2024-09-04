from django.urls import path
from .views import ai_respond

urlpatterns = [
    path('ai_respond/', ai_respond, name='ai_respond'),
]
