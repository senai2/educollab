from django.shortcuts import render

# Create your views here.
def index(request):
    current_user = request.user
    if current_user.id:
        return render(request, 'feeds.html', {})
    else:
        return render(request, 'index.html', {})
