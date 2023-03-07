from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_page, name='home'),
    path('team/', views.team_page, name='team'),
    path('project/', views.project_page, name='project'),
    path('about/', views.about_page, name='about'),
]