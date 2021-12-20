from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class TechGroup(models.Model):
    name = models.CharField("Name", max_length=25)
    order = models.IntegerField("Order")
    showAsSkill = models.BooleanField("Show as a skill", default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class Technology(models.Model):
    techGroup = models.ForeignKey(TechGroup, related_name="skills", on_delete=models.SET_NULL, null=True)
    name = models.CharField("Name", max_length=50)
    level = models.IntegerField("Level", validators=[MinValueValidator(1), MaxValueValidator(5)])
    isRelevant = models.BooleanField("Is relevant")
    showAsFilter = models.BooleanField("Show as a filter", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Technologies"
        ordering = ['-level']