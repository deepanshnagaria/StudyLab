from django.urls import path
from .views import InstitutionView

urlpatterns = [
        path('institution', InstitutionView.as_view())
]
