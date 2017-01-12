from django.db import models


class Account(models.Model):
    email = models.EmailField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
