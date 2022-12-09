from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Appointment(models.Model):
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    subject = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title