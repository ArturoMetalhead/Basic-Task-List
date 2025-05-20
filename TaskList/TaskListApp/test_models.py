from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):

    def setUp(self):
        # Create a sample task for testing
        self.task = Task.objects.create(title="Test Task", completed=False)
        self.task.save()
        self.task.refresh_from_db()  # Refresh to get the updated instance from the database

    def test_task_creation(self):
        # Check if the task was created successfully and has the correct attributes
        self.assertEqual(self.task.title, "Test Task")
        self.assertFalse(self.task.completed)
        self.assertIsNotNone(self.task.created_at)  # Ensure created_at is set

        # Check if the task is retrieved correctly from the database
        retrieved_task = Task.objects.get(id=self.task.id)
        self.assertEqual(retrieved_task.title, "Test Task")
        self.assertFalse(retrieved_task.completed)
        self.assertEqual(retrieved_task.created_at, self.task.created_at)
        
    def test_task_update(self):
        # Update the task and check if the changes are saved correctly
        self.task.title = "Updated Task"
        self.task.completed = True
        self.task.save()
        self.task.refresh_from_db()  # Refresh to get the updated instance from the database
        self.assertEqual(self.task.title, "Updated Task")
        self.assertTrue(self.task.completed)
        self.assertIsNotNone(self.task.created_at)  # Ensure created_at remains unchanged
        self.assertIsNotNone(self.task.updated_at)  # Ensure updated_at is set
        self.assertGreater(self.task.updated_at, self.task.created_at)  # Ensure updated_at is after created_at
        self.assertEqual(self.task.updated_at, self.task.updated_at)  # Ensure updated_at is consistent.