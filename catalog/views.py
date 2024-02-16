from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from catalog.models import Tag, Task


def complete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.is_done = True
    task.save()
    return render(request, "catalog/task_list.html", context={"task_list": Task.objects.all()})


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "catalog/task_list.html"
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("catalog:home")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("catalog:home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("catalog:home")







class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "catalog/tag_list.html"
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("catalog:home")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("catalog:home")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("catalog:home")
