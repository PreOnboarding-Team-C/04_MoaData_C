
from django.urls import path
from .views import JobDetailRUDViews, JobListView, JobTaskView

urlpatterns = [
    path('', JobListView.as_view()),
    path('/<int:id>', JobDetailRUDViews.as_view()),
    path('/<int:id>/run', JobTaskView.as_view())
]
