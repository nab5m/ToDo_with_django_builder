from django.views import generic
from . import models
from . import forms


class TaskListView(generic.ListView):
    model = models.Task
    form_class = forms.TaskForm


class TaskCreateView(generic.CreateView):
    model = models.Task
    form_class = forms.TaskForm


class TaskDetailView(generic.DetailView):
    model = models.Task
    form_class = forms.TaskForm


class TaskUpdateView(generic.UpdateView):
    model = models.Task
    form_class = forms.TaskForm
    pk_url_kwarg = "pk"
