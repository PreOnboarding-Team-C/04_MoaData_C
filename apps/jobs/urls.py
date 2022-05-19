from django.urls import path

from .views import JobCreateAPIView, JobDetailAPIView, TaskAPIView


urlpatterns = [
    path('', JobCreateAPIView.as_view()),
    path('/<int:job_id>', JobDetailAPIView.as_view()),
    path('/<int:job_id>/tasks', TaskAPIView.as_view()),
]
