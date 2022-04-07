from django.shortcuts import render
from .models import Room

# rooms = [
#     {'id':1,'name':'Lets learn py1'},
#     {'id':2,'name':'Lets learn py2'},
#     {'id':3,'name':'Lets learn py3'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'startup/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request,'startup/room.html',context)

def createRoom(request):
    context = {}
    return render(request,'startup/room_form.html',context)