import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_Task_list_view():
    instance1 = test_helpers.create_task_Task()
    instance2 = test_helpers.create_task_Task()
    client = Client()
    url = reverse("task_Task_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Task_create_view():
    client = Client()
    url = reverse("task_Task_create")
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Task_detail_view():
    client = Client()
    instance = test_helpers.create_task_Task()
    url = reverse("task_Task_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Task_update_view():
    client = Client()
    instance = test_helpers.create_task_Task()
    url = reverse("task_Task_update", args=[instance.pk, ])
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
