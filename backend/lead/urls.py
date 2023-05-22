from django.urls import path

from .views import LeadsAPIView

urlpatterns = [
    path("leads", LeadsAPIView.as_view()),
]
