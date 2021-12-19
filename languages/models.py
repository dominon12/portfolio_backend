from django.db import models


class Language(models.Model):
    name = models.CharField("Name", max_length=12)
    code = models.CharField("Language code", max_length=2)
    level = models.CharField("Level", max_length=10)
    learningHistory = models.TextField("Learning history")
    order = models.IntegerField("Ordering number")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']