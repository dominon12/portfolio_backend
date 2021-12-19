from django.db import models


class Profile(models.Model):
    firstName = models.CharField("First name", max_length=25)
    lastName = models.CharField("Last name", max_length=25)
    jobTitle = models.CharField("Job title", max_length=25)
    nickname = models.CharField("Nickname", max_length=25)
    cvDescription = models.TextField()
    photo = models.ForeignKey("components.Image", on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname


class AboutUnit(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="aboutUnits")
    title = models.CharField("Title", max_length=150)
    description = models.TextField("Description")
    image = models.ForeignKey("components.Image", on_delete=models.CASCADE)
    button = models.ForeignKey("components.Button", on_delete=models.CASCADE)
    order = models.IntegerField("Order")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title