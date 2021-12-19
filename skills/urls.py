from django.urls import path

from . import views 


app_name = 'skills'

urlpatterns = [
    path('grouped/', views.TechGroupList.as_view(), name='tech-group-list'),
]