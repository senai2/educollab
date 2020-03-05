from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('explore/', views.explore),
    path('signup/', views.signup),
    path('profile/', views.profile),
    path('subjects/<sid>', views.subject, name="subjects"),
    path('curriculum/new', views.create_curriculum),
    path('curriculum/<int:c_id>/edit', views.update_currilculum),
    path('curriculum/<int:c_id>/bit/new', views.create_bit),
    path('curriculum/<int:c_id>/bit/<int:b_id>/edit', views.update_bit)
]