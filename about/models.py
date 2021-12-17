from django.db import models


class AboutUnit(models.Model):
    title = models.CharField("Title", max_length=150)
    description = models.TextField("Description")
    image = models.ForeignKey("components.Image", on_delete=models.CASCADE)
    button = models.ForeignKey("components.Button", on_delete=models.CASCADE)
    order = models.IntegerField("Order")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
