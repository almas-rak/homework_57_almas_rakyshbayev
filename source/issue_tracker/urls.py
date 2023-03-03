from django.urls import path

from issue_tracker.views.tasks import IndexView, CreateTask

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("add/task/", CreateTask.as_view(), name='create_task'),
]
