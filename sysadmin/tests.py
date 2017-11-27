from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from sysadmin.models import MarkTask


class MartTaskTests(TestCase):
    def test_task_existed(self):
        """ently(), False)"""
        count = MarkTask.objects.all().count()
        self.assertFalse(count > 0)


class MartTaskViewTests(TestCase):
    def test_create(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.post(reverse('sysadmin:task_create'),
                                    data={"name": "test_name", "file_path": "c:/test/path/t.jpg"})
        self.assertEqual(response.status_code, 200)
