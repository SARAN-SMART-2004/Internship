# chatbot/urls.py

from django.urls import path
from .views import chatbot,index

urlpatterns = [
    path('chatbot/', chatbot, name='chatbot'),
    path('', index, name='index'),

]
