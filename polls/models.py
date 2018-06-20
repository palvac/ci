from django.db import models
from django.utils import timezone


class Poll(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created = models.DateField(default=timezone.now, null=True, blank=True)


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.PROTECT)
    text = models.CharField(max_length=255)
