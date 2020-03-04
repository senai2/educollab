from .models import Member
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

def view_profile(request, m_id, my_profile):
    app_member_details = get_object_or_404(Member, u_id=m_id)
    user_details = get_object_or_404(User, id=m_id)

    context = {
        'member' : app_member_details
    }
    return render(request, 'profile.html', context)