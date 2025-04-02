from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the category name.")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="subcategories")
    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=255, help_text="Enter the task name or description.")
    completed = models.BooleanField(default=False, help_text="Is the task completed?")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The time when the task was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="The time when the task was last updated.")
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks")
    def __str__(self):
        return f"{self.name} (Completed: {self.completed})"

