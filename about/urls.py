from django.urls import path

from . import views


app_name = "about"

urlpatterns = [
    path("about-units/", views.AboutUnitList.as_view(), name="about-unit-list"),
    path("profile/", views.ProfileDetail.as_view(), name="profile-detail"),
]