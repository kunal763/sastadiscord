from django.shortcuts import render,redirect
from .models import Topic,Message,Room
from .forms import RoomForm,Register
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
# rooms=[
#     {'name':'kunal','id':1},
#     {'name':'johny','id':2}
# ]

def home(request):
    q=request.GET.get('q') if request.GET.get('q')!=None else ""
    topics=Topic.objects.all()
    rooms=Room.objects.filter(Q(topic__name__icontains=q)|Q(name__icontains=q)|Q(host__username__icontains=q))
    return render(request,'base/index.html',{'rooms':rooms,'topics':topics})
def room(request,pk):
    room=Room.objects.get(id=pk)
    participants=room.participant.all()
    
    room_message=room.message_set.all().order_by('-created')
    if request.method=='POST':
        message=request.POST.get('message')
        Message.objects.create(
            room=room,
            user=request.user,
            text=message

        )
        room.participant.add(request.user)
        # participants.add(request.user)
        return redirect('room',pk=room.id)
    context={'room':room,'room_messages':room_message,'participants':participants}
    return render(request,'base/room.html',context)



@login_required(login_url='login')
def createRoom(request):
    form=RoomForm()
    if request.method=='POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request,'base/room_form.html',{'form':form})



@login_required(login_url='login')
def updateRoom(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)
    if request.method=='POST':
        form=RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request,'base/room_form.html',{'form':form})



@login_required(login_url='login')
def deleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    if request.method=='POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete_form.html',{'obj':room})

def login_room(request):
    context={'page':'login'}
    #this is so that if the user is authenticated then he can't go to the login page

    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username=request.POST.get('username').lower()
        password=request.POST.get('password')
        try:
            a=User.objects.get(username=username)
           
        except:
            messages.error(request, "User doesn't exist")
        a=authenticate(request,username=username,password=password)
        if a is not None:
            login(request,a)
            return redirect('home')
        else:
            messages.error(request,"Username or password doesn't exist")
    return render(request,'base/login_register.html',context)
def logoutRoom(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')

    return render(request,'base/logout.html',{})


def register(request):
    form=Register()
    if request.method=='POST':
        form=Register(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
    return render(request,'base/login_register.html',{'form':form})


@login_required(login_url='login')
def deleteMessage(request,pk,room_pk):
    message=Message.objects.get(id=pk)
    context={'obj':message}
    if request.method=='POST':
        message.delete()
        return redirect('room',room_pk)
    return render(request,'base/delete_form.html',context)