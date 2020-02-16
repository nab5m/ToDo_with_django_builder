from django.db import models
from django.urls import reverse


class Task(models.Model):

    #  Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=255)
    completion = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("task_Task_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("task_Task_update", args=(self.pk,))
