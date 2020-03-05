from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .utils import check_user_id, create_member_obj
from .forms import SignUpForm
from datetime import datetime
from app.models import Field, Subject
from app import curriculum

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

def profile(request):
    return render(request, 'profile.html', {})

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            create_member_obj(request.POST, user.id)
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

def create_curriculum(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return curriculum.createcurriculum(request)

def update_currilculum(request, c_id):
    if not request.user.is_authenticated:
        return redirect('login')
    return curriculum.updatecurriculum(request, c_id)

def create_bit(request, c_id):
    if not request.user.is_authenticated:
        return redirect('login')
    return curriculum.createbit(request, c_id)

def update_bit(request, c_id, b_id):
    if not request.user.is_authenticated:
        return redirect('login')
    return curriculum.updatebit(request, c_id, b_id)