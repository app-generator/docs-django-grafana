from django.db import models
from django.utils import timezone


class Transaction(models.Model):
    user_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Transaction: {self.user_id} - {self.amount} ({self.transaction_type})"
