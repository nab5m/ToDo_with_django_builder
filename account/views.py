from django.views import generic
from . import models
from . import forms


class AccountListView(generic.ListView):
    model = models.Account
    form_class = forms.AccountForm


class AccountCreateView(generic.CreateView):
    model = models.Account
    form_class = forms.AccountForm


class AccountDetailView(generic.DetailView):
    model = models.Account
    form_class = forms.AccountForm


class AccountUpdateView(generic.UpdateView):
    model = models.Account
    form_class = forms.AccountForm
    pk_url_kwarg = "pk"
