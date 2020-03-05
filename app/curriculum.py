from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .utils import check_user_id
from .forms import SignUpForm, CurriculumForm, BitForm
from datetime import datetime
from app.models import Field, Subject, Topic, Curriculum, Member, Bit

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
        
        bit.title = data.get("title"),
        bit.bit_type = data["bit_type"],
        bit.description = data["description"],
        bit.text = data["text"],
        bit.curriculum = Curriculum(id=c_id)
        
        bit.save()

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