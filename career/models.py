from django.db import models


class CareerEvent(models.Model):
    title = models.CharField("Title", max_length=100)
    description = models.TextField("Description", null=True, blank=True)
    date = models.DateField("Date")
    place = models.CharField("Place", max_length=50)
    isRelevant = models.BooleanField("Is relevant")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']