from django.urls import path 

from . import views 


app_name = 'languages'

urlpatterns = [
    path('', views.LanguageList.as_view(), name='languages-list'),
]