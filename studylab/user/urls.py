from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user/signup/$', views.NewUser.as_view()),
    url(r'^user/login$', views.Login.as_view()),
    url(r'^user/logout$', views.Logout.as_view()),
]
