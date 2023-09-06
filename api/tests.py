from django.test import TestCase
from django.urls import reverse

from .models import Task
# Create your tests here.

class TaskTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.task=Task.objects.create(
            title='Finish up on basic frontend',
            completed=True,
        )

    def test_task_content(self):
        self.assertEqual(self.task.title, 'Finish up on basic frontend')
        self.assertEqual(self.task.completed, True)

    

