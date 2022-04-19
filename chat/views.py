from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm
from .models import Message, Room


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def index(request):
    rooms = Room.objects.all()
    return render(request, 'chat/index.html', {'rooms': rooms})


def room(request, pk):
    room_name = Room.objects.get(pk=pk)
    messages = Message.objects.filter(room=room_name)[0:50:-1]
    return render(request, 'chat/room.html',
                  {'room': room_name,
                   'messages': messages})
