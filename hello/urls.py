from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("varun", views.varun, name = "varun"),
    path("devil", views.devil, name = "devil"),
    path("<str:name>", views.greet, name = "greet")
]