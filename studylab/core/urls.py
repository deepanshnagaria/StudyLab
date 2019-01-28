from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url('institution', views.InstitutionView.as_view()),
    url('subjects', views.SubjectsView.as_view()),
]
