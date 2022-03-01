from django.db import models


class Article(models.Model):
    title = models.CharField("Title", max_length=150)
    slug = models.SlugField("Slug")
    description = models.TextField("Description")
    image = models.ForeignKey("components.Image", on_delete=models.SET_NULL, null=True)
    body = models.TextField("Body")
    viewers = models.ManyToManyField("users.AnonymousUser", blank=True)
    dateCreated = models.DateTimeField("Date created", auto_now_add=True)
    dateEdited = models.DateTimeField("Date edited", auto_now=True)

    class Meta:
        ordering = ['-dateCreated']

    def __str__(self):
        return self.title

