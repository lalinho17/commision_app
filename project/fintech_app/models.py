from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models




class Account(models.Model):
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    def _str_(self):
        return f"{self.user.username} - {self.account_number}"


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="transactions")
    transaction_type = models.CharField(max_length=10, choices=[("deposit", "Deposit"), ("withdrawal", "Withdrawal")])
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.transaction_type} - {self.amount} on {self.timestamp}"

    
