from django.contrib.auth.models import User
from .models import Member

def check_user_id(user):
    if not Member.objects.filter(u_id=user.id):
        m_obj = Member(
            u_id = user,
            username = user.username,
            email = user.email, 
        )
        m_obj.save()
    return 1

def create_member_obj(user, u_id):
    m_obj = Member(
        u_id = User(id=u_id),
        username = user['username'],
        email = user['email'],
        full_name = user['first_name'] + ' ' + user['last_name'],
        institution = user['institution'],
        designation = user['designation']
    )
    m_obj.save()