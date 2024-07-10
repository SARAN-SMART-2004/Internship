# chatbot/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .chatbot_logic import get_intent, get_response

def chatbot(request):
    if request.method == "POST":
        user_message = request.POST.get('message')
        intent = get_intent(user_message)
        bot_response = get_response(intent)
        return JsonResponse({"response": bot_response})
    return render(request, "chatbot/chatbot.html")
def index(request):
    return render(request, "chatbot/index.html")