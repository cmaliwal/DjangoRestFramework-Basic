from __future__ import unicode_literals

from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=20)
    task_desc = models.TextField(max_length=200)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "%s" % self.task_name