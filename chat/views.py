from django.shortcuts import render
from chat.models import Message
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
import json
# Create your views here.

def index(request):
    return render(request, "chat/index.html")

@login_required(login_url="index")
def room(request, room_name):
    room_chat_history = Message.objects.filter(room_name=room_name)
    room_chat_history = [f"{chat.user.username} says: {chat.text} | {chat.created.date()} at {chat.created.hour}:{chat.created.minute}" for chat in room_chat_history]
    return render(request, "chat/room.html", {"room_name": room_name, "history":json.dumps(room_chat_history)})


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("index")
        else:
            print("error")
            messages.error(request, "wrong creadentials")
    return redirect("index")