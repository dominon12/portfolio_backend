from django.db import models


class Project(models.Model):
    PROJECT_TYPES = (
        ("Bot", "Bot"),
        ("Web app", "Web app"),
        ("REST API", "REST API"),
        ("E-commerce", "E-commerce"),
        ("Landing", "Landing"),
        ("Library", "Library")
    )

    name = models.CharField("Name", max_length=150)
    shortDescription = models.CharField("Short description", max_length=250)
    description = models.TextField("Description")
    image = models.ForeignKey("components.image", on_delete=models.CASCADE)
    type = models.CharField("Type", max_length=15, choices=PROJECT_TYPES)
    date = models.DateField("Date started")
    implementationTime = models.IntegerField("Time of implementation")
    link = models.URLField("Project url", null=True, blank=True)
    repository = models.URLField("Repository url", null=True, blank=True)
    technologies = models.ManyToManyField("skills.Technology")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.link

    class Meta:
        ordering = ['-date']
