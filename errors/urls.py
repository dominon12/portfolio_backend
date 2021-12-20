from django.urls import path

from . import views 


app_name = 'errors'

urlpatterns = [
    path('error-feedback/', views.ErrorFeedbackCreate.as_view(), name='error-feedback-create'),
    path('client-error/', views.ClientErrorCreate.as_view(), name='client-error-create'),
]