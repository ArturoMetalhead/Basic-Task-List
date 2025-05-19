from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from .models import Task

class TaskListE2ETest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_add_and_delete_task(self):

        #SIMPLE TASK

        # Open the home page
        self.selenium.get(self.live_server_url)
        time.sleep(2)  # Wait for the page to load
        # Add a new task
        task_input = self.selenium.find_element(By.ID, 'taskInput')
        task_input.send_keys('Test Task')
        task_input.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for the task to be added
        # Verify the task is added
        tasks = self.selenium.find_elements(By.CSS_SELECTOR, '.task-item')
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].text, 'Test Task')
        # Delete the task
        delete_checkbox = self.selenium.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
        delete_checkbox.click()
        time.sleep(2)  # Wait for the task to be deleted
        # Verify the task is deleted
        tasks = self.selenium.find_elements(By.CSS_SELECTOR, '.task-item')
        self.assertEqual(len(tasks), 0)

        print("SIMPLE TASK DONE")

        #LINK

        # Add a new task with a link
        task_input = self.selenium.find_element(By.ID, 'taskInput')
        task_input.send_keys('Test Task with link: https://example.com')
        task_input.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for the task to be added
        # Verify the task is added with the link highlighted
        tasks = self.selenium.find_elements(By.CSS_SELECTOR, '.task-item')
        self.assertEqual(len(tasks), 1)
        self.assertIn('Test Task with link:', tasks[0].text)
        self.assertIn('https://example.com', tasks[0].text)
        self.assertIn('<a href="https://example.com" target="_blank">https://example.com</a>', tasks[0].get_attribute('innerHTML'))
        # Delete the task
        delete_checkbox = self.selenium.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
        delete_checkbox.click()
        time.sleep(2)  # Wait for the task to be deleted
        # Verify the task is deleted
        tasks = self.selenium.find_elements(By.CSS_SELECTOR, '.task-item')
        self.assertEqual(len(tasks), 0)

        print("LINK DONE")

        #EMAIL

        # Add a new task with an email
        task_input = self.selenium.find_element(By.ID, 'taskInput')
        task_input.send_keys('Test Task with email: test@example.com')
        task_input.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for the task to be added
        # Verify the task is added with the email highlighted
        tasks = self.selenium.find_elements(By.CSS_SELECTOR, '.task-item')
        self.assertEqual(len(tasks), 1)
        self.assertIn('Test Task with email:', tasks[0].text)
        self.assertIn('test@example.com', tasks[0].text)
        self.assertIn('<a href="mailto:test@example.com">test@example.com</a>', tasks[0].get_attribute('innerHTML'))
        # Delete the task
        delete_checkbox = self.selenium.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
        delete_checkbox.click()
        time.sleep(2)  # Wait for the task to be deleted
        # Verify the task is deleted
        tasks = self.selenium.find_elements(By.CSS_SELECTOR, '.task-item')
        self.assertEqual(len(tasks), 0)

        print("EMAIL DONE")

        #URL with www

        # Add a new task with a URL starting with www
        task_input = self.selenium.find_element(By.ID, 'taskInput')
        task_input.send_keys('Test Task with URL: www.example.com')
        task_input.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for the task to be added
        # Verify the task is added with the URL highlighted
        tasks = self.selenium.find_elements(By.CSS_SELECTOR, '.task-item')
        self.assertEqual(len(tasks), 1)
        self.assertIn('Test Task with URL:', tasks[0].text)
        self.assertIn('www.example.com', tasks[0].text)
        self.assertIn('<a href="http://www.example.com" target="_blank">www.example.com</a>', tasks[0].get_attribute('innerHTML'))
        # Delete the task
        delete_checkbox = self.selenium.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
        delete_checkbox.click()
        time.sleep(2)  # Wait for the task to be deleted
        # Verify the task is deleted
        tasks = self.selenium.find_elements(By.CSS_SELECTOR, '.task-item')
        self.assertEqual(len(tasks), 0)

        print("WWW DONE")

        #URL with http

        # Add a new task with a URL starting with http
        task_input = self.selenium.find_element(By.ID, 'taskInput')
        task_input.send_keys('Test Task with URL: http://example.com')
        task_input.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for the task to be added
        # Verify the task is added with the URL highlighted
        tasks = self.selenium.find_elements(By.CSS_SELECTOR, '.task-item')
        self.assertEqual(len(tasks), 1)
        self.assertIn('Test Task with URL:', tasks[0].text)
        self.assertIn('http://example.com', tasks[0].text)
        self.assertIn('<a href="http://example.com" target="_blank">http://example.com</a>', tasks[0].get_attribute('innerHTML'))
        # Delete the task
        delete_checkbox = self.selenium.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
        delete_checkbox.click()
        time.sleep(2)  # Wait for the task to be deleted
        # Verify the task is deleted
        tasks = self.selenium.find_elements(By.CSS_SELECTOR, '.task-item')
        self.assertEqual(len(tasks), 0)

        print("HTTP DONE")

        #URL with https

        # Add a new task with a URL starting with http/https
        task_input = self.selenium.find_element(By.ID, 'taskInput')
        task_input.send_keys('Test Task with URL: https://example.com')
        task_input.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for the task to be added
        # Verify the task is added with the URL highlighted
        tasks = self.selenium.find_elements(By.CSS_SELECTOR, '.task-item')
        self.assertEqual(len(tasks), 1)
        self.assertIn('Test Task with URL:', tasks[0].text)
        self.assertIn('https://example.com', tasks[0].text)
        self.assertIn('<a href="https://example.com" target="_blank">https://example.com</a>', tasks[0].get_attribute('innerHTML'))
        # Delete the task
        delete_checkbox = self.selenium.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
        delete_checkbox.click()
        time.sleep(2)  # Wait for the task to be deleted
        # Verify the task is deleted
        tasks = self.selenium.find_elements(By.CSS_SELECTOR, '.task-item')
        self.assertEqual(len(tasks), 0)

        print("HTTPS DONE")
