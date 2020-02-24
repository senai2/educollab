from django.contrib.auth.models import User
from .models import Member

def check_user_id(user):
    if not Member.objects.filter(u_id=user.id):
        print(user)
        m_obj = Member(
            u_id = user,
            username = user.username,
            email = user.email, 
        )
        m_obj.save()
    return 1

