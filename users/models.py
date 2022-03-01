from ipaddress import ip_address
from django.db import models


class AnonymousUser(models.Model):
    ipAddress = models.GenericIPAddressField("IP address")

    def __str__(self):
        return self.ipAddress
