from django.urls import path
from . import views
# from rest_framework import routers
# from testpaper.views import QuestionsViewSet



# router = routers.DefaultRouter()
# router.register(r'questions',QuestionsViewSet,base_name="questions")


urlpatterns = [
        path('testpaper/create/', views.TestPaperView.as_view()),
        path('questions/', views.QuestionsView.as_view()),
        path('test/',views.TestView.as_view()),
        path('questions/upload',views.FileView.as_view())
]