from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .utils import check_user_id
from .forms import SignUpForm
from .profile import view_profile, edit_profile

# Create your views here.
def index(request):
    current_user = request.user
    if current_user.id:
        check_user_id(current_user)
        return render(request, 'feeds.html', {})
    else:
        return render(request, 'index.html', {})

def profile(request,uname):
    if not request.user.is_authenticated:
        return redirect('login')
    return view_profile(request, uname)

def myprofile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return view_profile(request, request.user.username)

def editprofile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return edit_profile(request)

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