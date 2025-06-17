from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings


CATEGORY_CHOICES = (
    ('Food', 'Food'),
    ('Transport', 'Transport'),
    ('Shopping', 'Shopping'),
    ('Entertainment', 'Entertainment'),
    ('Bills', 'Bills'),
    ('Other', 'Other'),
    ('Salary', 'Salary'),
    ('Freelance', 'Freelance'),
    ('Investment', 'Investment'),
    ('Gift', 'Gift'),
    ('Other', 'Other'),
)


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.source} - ₹{self.amount}"


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    description = models.TextField(blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.category} - ₹{self.amount}"

class Budget(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    monthly_limit = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.username} - ₹{self.monthly_limit}"