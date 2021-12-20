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