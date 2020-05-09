from django.db import models


class Webs(models.Model):
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'webs'

    def __str__(self):
        return self.text
