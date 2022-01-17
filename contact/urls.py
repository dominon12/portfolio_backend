from django.urls import path

from . import views     


app_name = 'contact'

urlpatterns = [
    path('contact-method/', views.ContactMethodList.as_view(), name='contact-methods-list'),
    path('contact-request/', views.ContactRequestCreate.as_view(), name='contact-request-create'),
    path('order/', views.ReportOrder.as_view(), name="report-order")
]