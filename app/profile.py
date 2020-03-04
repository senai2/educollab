from .models import Member, Curriculum, Bit, Upvote, Comment
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

def view_profile(request, uname):
    app_member_details = get_object_or_404(Member, username=uname)
    user_details = get_object_or_404(User, username=uname)
    
    curriculums = Curriculum.objects.filter(posted_by=user_details.id)

    c_list = []
    for c in curriculums:
        bits = Bit.objects.filter(curriculum=c)
        b_list = []

        for b in bits:
            b_obj = b.__dict__
            b_obj["likes"] = len(Upvote.objects.filter(bit=b))
            b_obj["comments"] = len(Comment.objects.filter(bit=b))

            b_list.append(b_obj)

        c_obj = c.__dict__
        c_obj["b_list"] = b_list
        
        c_list.append(c_obj)

    context = {
        'member' : app_member_details,
        'c_list' : c_list,
        'name' : user_details.first_name + ' ' + user_details.last_name,
        'my_profile' : request.user.username==uname
    }
    return render(request, 'profile.html', context)