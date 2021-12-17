from django.urls import path

from . import views     


app_name = 'contact'

urlpatterns = [
    path('contact-method/', views.ContactMethodList.as_view(), name='contact-methods-list'),
]