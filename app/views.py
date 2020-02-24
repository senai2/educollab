from django.shortcuts import render
from .utils import check_user_id

# Create your views here.
def index(request):
    current_user = request.user
    if current_user.id:
        check_user_id(current_user)
        return render(request, 'feeds.html', {})
    else:
        return render(request, 'index.html', {})

def signup(request):
    return render(request, 'registration/signup.html')