from django.urls import path

from issue_tracker.views.tasks import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
]
