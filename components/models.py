from django.db import models
from django.core.validators import MinValueValidator


class Button(models.Model):
    text = models.CharField("Text", max_length=20)
    link = models.CharField("Link", max_length=50)

    def __str__(self):
        return self.text


class Image(models.Model):
    image = models.ImageField("Image", upload_to="about")
    alt = models.CharField("Alt", max_length=150)
    width = models.IntegerField("Width", validators=[MinValueValidator(0)])
    height = models.IntegerField("Height", validators=[MinValueValidator(0)])

    def __str__(self):
        return self.alt