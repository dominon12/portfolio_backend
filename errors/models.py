from django.db import models

from . import tasks


class ErrorFeedback(models.Model):
    comment = models.TextField("Comment")
    date = models.DateTimeField("Date", auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['-date']

    def save(self, *args, **kwargs):
        if not self.pk:
            tasks.on_new_error_feedback.delay(
                comment=self.comment
            )

        super().save(*args, **kwargs)


class ClientError(models.Model):
    name = models.CharField(max_length=150)
    message = models.TextField(blank=True, null=True)
    url = models.URLField()
    userAgent = models.TextField()
    ipAddress = models.GenericIPAddressField()
    componentStack = models.TextField()
    stack = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            tasks.on_new_client_error.delay(
                name=self.name,
                message=self.message,
                url=self.url,
                user_agent=self.userAgent,
                ip_address=self.ipAddress
            )
        super().save(*args, **kwargs)