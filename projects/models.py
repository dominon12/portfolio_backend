from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.link

    class Meta:
        ordering = ['-date']


class Technology(models.Model):
    name = models.CharField("Name", max_length=50)
    level = models.IntegerField("Level", validators=[MinValueValidator(1), MaxValueValidator(5)])
    isRelevant = models.BooleanField("Is relevant")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Technologies"


class TechStack(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name="technologies")
    backend = models.ManyToManyField(Technology, verbose_name="Backend", related_name="tech_stack_backend")
    frontend = models.ManyToManyField(Technology, verbose_name="Frontend", related_name="tech_stack_frontend")
    devops = models.ManyToManyField(Technology, verbose_name="DevOps", related_name="tech_stack_devops")

    def __str__(self):
        return f"{self.project.name} technologies"
