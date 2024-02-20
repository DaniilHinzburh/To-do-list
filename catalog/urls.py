from django.contrib import admin
from django.urls import path

from catalog.views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, CompleteTaskView, TagListView, \
    TagCreateView, TagUpdateView, TagDeleteView

app_name = "catalog"
urlpatterns = [
    path(
        "",
        TaskListView.as_view(),
        name="home",
    ),
    path(
        "task/create/",
        TaskCreateView.as_view(),
        name="task_create",
    ),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task_update",
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task_delete",
    ),
    path(
        "task/<int:pk>/complete/",
        CompleteTaskView.as_view(),
        name="task_complete",
    ),

    path(
        "tag/",
        TagListView.as_view(),
        name="tag_list",
    ),
    path(
        "tag/create/",
        TagCreateView.as_view(),
        name="tag_create",
    ),
    path(
        "tag/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag_update",
    ),
    path(
        "tag/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag_delete",
    ),

]
