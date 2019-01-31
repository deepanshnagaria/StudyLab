from django.urls import path
from . import views

urlpatterns = [
        path('testpaper/create/', views.TestPaperView.as_view()),
        path('questions/', views.QuestionsView.as_view()),
]