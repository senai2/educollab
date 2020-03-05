from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from .utils import check_user_id
from .forms import SignUpForm, CurriculumForm, BitForm
from datetime import datetime
from app.models import Field, Subject, Topic, Curriculum, Member, Bit

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

def createcurriculum(request):

    # dropdown list to choose
    fields = Field.objects.all()
    topics = Topic.objects.all()
    subjects = Subject.objects.all()

    form_type = 'Create'

    if request.method == 'POST':
        data = request.POST
        c_obj = Curriculum(
            title = data['title'],
            subject = Subject(id=data['subjects']),
            description = data['description'],
            posted_by = Member(id=request.user.id)
        )

        c_obj.save()
        #TODO: Add entry in changelog but what is comment field?

        context = {
            'success' : 'Curriculum created!'
        }
        return render(request, 'curriculum-form.html', context)
    else:
        form = CurriculumForm()
        context = {
            'form' : form,
            'type' : form_type,
            'fields' : fields,
            'topics' : topics,
            'subjects' : subjects
        }
        return render(request, 'curriculum-form.html', context)

def updatecurriculum(request, c_id):
    # dropdown list menu to choose
    fields = Field.objects.all()
    topics = Topic.objects.all()
    subjects = Subject.objects.all()

    curriculum = get_object_or_404(Curriculum, id=c_id)
    form_type = 'Update'

    if request.method == 'POST':
        data = request.POST

        curriculum.title = data["title"]
        curriculum.subject = Subject(id=data['subjects'])
        curriculum.description = data['description']

        curriculum.save()
        #TODO: Add entry in changelog

        context = {
            'success' : 'Curriculum updated!'
        }
        return render(request, 'curriculum-form.html', context)
    else:
        
        form = CurriculumForm(data=curriculum.__dict__)
        context = {
            'form' : form,
            'type' : form_type,
            'fields' : fields,
            'topics' : topics,
            'subjects' : subjects
        }
        return render(request, 'curriculum-form.html', context)

def createbit(request, c_id):
    curriculum = get_object_or_404(Curriculum, id=c_id)
    form_type = 'Create'
    if request.method == 'POST':
        data = request.POST
        b_obj = Bit(
            title = data["title"],
            bit_type = data["bit_type"],
            description = data["description"],
            text = data["text"],
            curriculum = Curriculum(id=c_id)
        )
        b_obj.save()
        context = {
            'success' : 'Bit Added!'
        }
        return render(request, 'bit-form.html', context)
    else:
        form = BitForm()
        context = {
            'curriculum' : curriculum,
            'form' : form,
            'type' : form_type
        }
        return render(request, 'bit-form.html', context)


def updatebit(request, c_id, b_id):
    curriculum = get_object_or_404(Curriculum, id=c_id)
    bit = get_object_or_404(Bit, id=b_id)
    form_type = 'Update'
    if request.method == 'POST':
        data = request.POST
        
        #print(data)
        
        bit.title = data.get("title"),
        bit.bit_type = data["bit_type"],
        bit.description = data["description"],
        bit.text = data["text"],
        bit.curriculum = Curriculum(id=c_id)
        print(bit.__dict__)
        # bit.save()

        context = {
            'success' : 'Bit Updated!'
        }
        return render(request, 'bit-form.html', context)
    else:
        form = BitForm(data=bit.__dict__)
        context = {
            'curriculum' : curriculum,
            'form' : form,
            'type' : form_type
        }
        return render(request, 'bit-form.html', context)