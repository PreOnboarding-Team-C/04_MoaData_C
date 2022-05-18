from django.urls import path
from apps.job.views import JsonAPI, JsonDetailAPI, JobTaskAPI

urlpatterns = [
    path('', JsonAPI.as_view()),
    path('/<int:job_id>', JsonDetailAPI.as_view()),
    path('/<int:job_id>/run', JobTaskAPI.as_view()),
]