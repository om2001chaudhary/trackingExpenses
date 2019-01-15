from django.db import models
from django.contrib.auth.models import User
import datetime

class ClientExpense(models.Model):

    client = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(max_length=200)
    amount = models.IntegerField(blank=False)
    currency = models.CharField(max_length=10)
    description = models.CharField(max_length=1000)
    date = models.DateField(default=datetime.date.today)
    class Meta:
        db_table = 'client_expense'