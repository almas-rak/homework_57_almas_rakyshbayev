from django.urls import path

from issue_tracker.views.tasks import IndexView, CreateTask, TaskDetail

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("add/task/", CreateTask.as_view(), name='create_task'),
    path('detail/task/<int:pk>', TaskDetail.as_view(), name='task_detail'),
]
