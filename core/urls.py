from django.urls import path

from . import views

urlpatterns = [
    path("unlock/", views.unlock, name="unlock"),
    path("", views.index, name="index"),
]

app_name = "core"