from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import Room


@login_required
def rooms_list(request):
    rooms = Room.objects.all().values('name')

    return render(request, 'room/rooms_list.html', {'rooms': rooms})


@login_required
def room_detailed(request, pk):
    room = Room.objects.get(pk=pk)

    return render(request, 'room/room_detailed.html', {'room': room})
