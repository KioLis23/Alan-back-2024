from django.db import models

class Message(models.Model):
    author = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}: {self.message}"
