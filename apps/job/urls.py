from django.urls import path
from apps.job.views import JsonAPI

urlpatterns = [
    path('/json', JsonAPI.as_view()),
    path('/json/<int:job_id>', JsonAPI.as_view()),
]