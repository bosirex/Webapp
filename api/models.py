from django.db import models

class NeedHelp(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    acceleration = models.FloatField(null=True)
    status = models.CharField(max_length=50, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username