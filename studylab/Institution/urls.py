from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
        url('center', views.CenterView.as_view()),
]
