from django.shortcuts import render

from .models import Message, Room


def index(request):
    rooms = Room.objects.all()
    return render(request, 'chat/index.html', {'rooms': rooms})


def room(request, pk):
    room_name = Room.objects.get(pk=pk)
    messages = Message.objects.filter(room=room_name)[0:50:-1]
    return render(request, 'chat/room.html',
                  {'room': room_name,
                   'messages': messages})
