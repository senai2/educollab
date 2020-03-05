from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .utils import check_user_id
from .forms import SignUpForm, NewCurriculum
from datetime import datetime
from app.models import Field, Subject

# Create your views here.
def index(request):
    current_user = request.user

    # todo: bind to some model / facade design pattern
    # so logs and and other stuff can be combined
    # also -> showing "bits" of a curriculum is difficult
    # rather link to that view
    feeds = { "1":
            {
                "title": "Log Entry Title A - Curriculum Updated",
                "text":  "lorem ispum",
                "date": datetime.now()
            },
        "2":
            {
                "title": "Log Entry Title B - Curriculum Created",
                "text":  "lorem ispum",
                "date": datetime.now()
            }
    }
    if current_user.id:
        check_user_id(current_user)
        return render(request, 'feeds.html', {
            "feeds": feeds
        })
    else:
        return render(request, 'index.html', {})

# def signup(request):
#     return render(request, 'registration/signup.html')

def profile(request):
    return render(request, 'profile.html', {})

def new_curriculum(request):
    if request.method == 'POST':
        form = NewCurriculum(request.POST)
        
        if form.is_valid():
            return redirect('home') #For now
    else:
        form = NewCurriculum()
    
    return render(request, 'new_curriculum.html', {'form':form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            form = SignUpForm()
        
    return render(request, 'registration/signup.html', {'form': form})


def explore(request):
    fields = Field.objects.all()
    return render(request, 'explore.html', {"fields": fields})


def subject(request, sid):
    subject = Subject.objects.filter(id=sid).first()
    context = {
        'subject': subject
    }
    return render(request, 'subject.html', context)
