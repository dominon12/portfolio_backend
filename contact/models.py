from django.db import models


class ContactMethod(models.Model):
    name = models.CharField("Name", max_length=50)
    link = models.URLField("Link")

    def __str__(self):
        return self.name