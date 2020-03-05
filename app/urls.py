from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('explore/', views.explore),
    path('signup/', views.signup),
    path('profile/', views.profile),
    path('new_curriculum/', views.new_curriculum),
    path('subjects/<sid>', views.subject, name="subjects"),
]