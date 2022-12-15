from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import RegexValidator
from .validators import validate_text


class Appointment(models.Model):
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=30, validators=[validate_text, RegexValidator(r'^[\w\s.,:;\'"]*$')])
    subject = models.TextField(max_length=200, validators=[validate_text, RegexValidator(r'^[\w\s.,:;\'"]*$')])
    date = models.DateTimeField(unique=True)

    def __str__(self):
        return self.title
