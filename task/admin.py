from django.contrib import admin
from django import forms

from . import models


class TaskAdminForm(forms.ModelForm):

    class Meta:
        model = models.Task
        fields = "__all__"


class TaskAdmin(admin.ModelAdmin):
    form = TaskAdminForm
    list_display = [
        "created",
        "name",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "name",
        "last_updated",
    ]


admin.site.register(models.Task, TaskAdmin)
