from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('explore/', views.explore),
    path('signup/', views.signup),
    path('profile/', views.profile),
    path('subjects/<sid>', views.subject, name="subjects"),
    path('create-curriculum/', views.createcurriculum),
    path('update-curriculum/<int:c_id>', views.updatecurriculum),
    path('<int:c_id>/create-bit', views.createbit),
    path('<int:c_id>/update-bit/<int:b_id>', views.updatebit)
]