from django.urls import path 

from . import views 


app_name = 'donations'

urlpatterns = [
    path('methods/', views.DonationMethodList.as_view(), name='donation-methods-list'),
]
