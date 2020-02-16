from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Task", api.TaskViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("task/Task/", views.TaskListView.as_view(), name="task_Task_list"),
    path("task/Task/create/", views.TaskCreateView.as_view(), name="task_Task_create"),
    path("task/Task/detail/<int:pk>/", views.TaskDetailView.as_view(), name="task_Task_detail"),
    path("task/Task/update/<int:pk>/", views.TaskUpdateView.as_view(), name="task_Task_update"),
)
