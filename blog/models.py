from django.urls import reverse
from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(
        "auth.user",
        on_delete=models.CASCADE
    )
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("todo_detail", kwargs={"pk": self.pk})