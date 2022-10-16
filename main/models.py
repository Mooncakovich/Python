from unittest.util import _MAX_LENGTH
from django.db import models

class Note(models.Model):
    title = models.CharField('Title', max_length=25)
    description = models.TextField('Description')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
