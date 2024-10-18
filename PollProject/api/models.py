
from django.db import models
from pollsapp.models import Poll, Choice

class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user = models.CharField(max_length=255)