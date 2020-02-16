from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Account", api.AccountViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("account/Account/", views.AccountListView.as_view(), name="account_Account_list"),
    path("account/Account/create/", views.AccountCreateView.as_view(), name="account_Account_create"),
    path("account/Account/detail/<int:pk>/", views.AccountDetailView.as_view(), name="account_Account_detail"),
    path("account/Account/update/<int:pk>/", views.AccountUpdateView.as_view(), name="account_Account_update"),
)
