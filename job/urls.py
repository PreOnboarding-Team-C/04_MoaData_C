
from django.urls import path
from .views import JobDetailRUDViews, JobListView, JobTaskView

urlpatterns = [
    path('jobs', JobListView.as_view()),
    path('jobs/<int:id>', JobDetailRUDViews.as_view()),
    path('jobs/<int:id>/run', JobTaskView.as_view())
]
