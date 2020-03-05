from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('explore/', views.explore),
    path('signup/', views.signup),
    path('profile/', views.profile),
    path('subjects/<sid>', views.subject, name="subjects"),
    path('curriculum/', views.curriculum_index, name="curriculum_index"),
    path('curriculum/new', views.curriculum_create, name="curriculum_create"),
    path('curriculum/<int:c_id>', views.curriculum_show, name="curriculum_show"),
    path('curriculum/<int:c_id>/edit',
         views.curriculum_update, name="curriculum_update"),
    path('curriculum/<int:c_id>/bit/new', views.create_bit),
    path('curriculum/<int:c_id>/bit/<int:b_id>/edit', views.update_bit),
    path('comment/<str:c_type>/<int:c_id>', views.comment)
]
