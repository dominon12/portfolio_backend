from django.urls import path

from . import views 


app_name = 'career'

urlpatterns = [
    path('', views.CareerEventList.as_view(), name='career-event-list'),
]