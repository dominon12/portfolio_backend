from django.db import models


class ContactMethod(models.Model):
    name = models.CharField("Name", max_length=50)
    link = models.CharField("Link", max_length=250)
    order = models.IntegerField("Ordering number")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']