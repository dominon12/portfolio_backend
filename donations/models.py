from django.db import models


class DonationMethod(models.Model):
    name = models.CharField("Name", max_length=20)
    comment = models.TextField("Comment")
    link = models.CharField("Link", max_length=250)
    isLink = models.BooleanField("Is link", default=True)
    image = models.ForeignKey("components.Image", on_delete=models.CASCADE)

    def __str__(self):
        return self.name