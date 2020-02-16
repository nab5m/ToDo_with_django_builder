from django.contrib import admin
from django import forms

from . import models


class AccountAdminForm(forms.ModelForm):

    class Meta:
        model = models.Account
        fields = "__all__"


class AccountAdmin(admin.ModelAdmin):
    form = AccountAdminForm
    list_display = [
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


admin.site.register(models.Account, AccountAdmin)
