from django.db import models

class SimpleMessage(models.Model):
    username = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)  # commented out for simplicity

    def __str__(self):
        return self.username



