from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, RedirectView

from issue_tracker.forms.form_task import TaskForm
from issue_tracker.models import Task


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(is_deleted=False)
        return context


class CreateTask(TemplateView):
    template_name = 'add_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm()
        return context

    def post(self, request: WSGIRequest, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('index')
        return render(request, 'add_task.html', context={'form': form})
