from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url('core/institution/', views.InstitutionView.as_view()),
    url('core/subjects', views.SubjectsView.as_view()),
    url('core/phase', views.PhaseView.as_view()),
]
