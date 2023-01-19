from django.utils import timezone
from django.db import models
from django.urls import reverse

# Create your models here.

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    completed = models.BooleanField(default=False,blank=False)
    important = models.BooleanField(default=False, blank=False)


    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["due_date"]