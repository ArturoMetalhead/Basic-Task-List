from django.test import TestCase, Client
from django.urls import reverse
from .models import Task


class TaskViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.task = Task.objects.create(title="Initial Task")

    def test_home_view_status_code_and_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'TaskListApp/home.html')
        self.assertIn(self.task, response.context['tasks'])

    def test_add_new_task(self):
        response = self.client.post(reverse('add_task'), {'title': 'New Task'})
        self.assertEqual(response.status_code, 302)  # redirect
        self.assertTrue(Task.objects.filter(title='New Task').exists())

    def test_add_empty_title_does_not_create(self):
        count_before = Task.objects.count()
        response = self.client.post(reverse('add_task'), {'title': '   '})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), count_before)

    def test_update_existing_task(self):
        response = self.client.post(reverse('add_task'), {
            'task_id': self.task.id,
            'title': 'Updated Task'
        })
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')

    def test_update_existing_task_to_empty_deletes(self):
        task_id = self.task.id
        response = self.client.post(reverse('add_task'), {
            'task_id': task_id,
            'title': '   '
        })
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=task_id).exists())

    def test_delete_task(self):
        response = self.client.post(reverse('delete_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

