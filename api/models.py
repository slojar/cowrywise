import uuid

from django.db import models


class Answer(models.Model):
    key = models.DateTimeField(auto_now_add=True)
    value = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return f'{self.key}'

