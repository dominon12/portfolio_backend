from django.db import models

from . import tasks


class ContactMethod(models.Model):
    name = models.CharField("Name", max_length=50)
    link = models.CharField("Link", max_length=250)
    order = models.IntegerField("Ordering number")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class ContactRequest(models.Model):
    name = models.CharField("Name", max_length=150)
    email = models.EmailField("Email")
    comment = models.TextField("Comment", blank=True, null=True)
    date = models.DateTimeField("Date", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']

    def save(self, *args, **kwargs):
        if not self.pk:
            tasks.on_new_contact_request.delay(
                name=self.name,
                email=self.email,
                comment=self.comment
            )

        super().save(*args, **kwargs)