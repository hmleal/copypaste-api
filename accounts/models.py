from django.db import models


class Account(models.Model):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class Message(models.Model):
    origin = models.ForeignKey(Account, related_name='origin_account')
    destination = models.ForeignKey(Account, related_name='destination_account')
    content = models.TextField()

    class Meta:
        unique_together = (('origin', 'destination'),)

    def __str__(self):
        return '{0} -> {1}: {2}'.format(
            self.origin, self.destination, self.content)
