from django.urls import path

from . import views


app_name = "about"

urlpatterns = [
    path("about-units/", views.AboutUnitList.as_view(), name="about-unit-list")
]