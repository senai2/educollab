from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .utils import check_user_id
from .forms import SignUpForm

# Create your views here.
def index(request):
    current_user = request.user
    if current_user.id:
        check_user_id(current_user)
        return render(request, 'feeds.html', {})
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