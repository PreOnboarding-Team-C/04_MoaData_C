from django.urls import path

from .views import JobAPIView


urlpatterns = [
    path('/jobs', JobAPIView.as_view()),
]
