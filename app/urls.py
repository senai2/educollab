from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('explore/', views.explore),
    path('signup/', views.signup),
    path('profile/', views.profile),
    path('subjects/<sid>', views.subject, name="subjects"),
    path('create-curriculum/', views.create_curriculum),
    path('update-curriculum/<int:c_id>', views.update_currilculum),
    path('<int:c_id>/create-bit', views.create_bit),
    path('<int:c_id>/update-bit/<int:b_id>', views.update_bit)
]