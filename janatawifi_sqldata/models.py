from django.db import models

# Create your models here.
class jatatawifi_stock_market(models.Model):
    date = models.DateField()
    trade_code=models.CharField(max_length=100)
    high = models.CharField( max_length=100)
    low = models.CharField(max_length=100)
    open = models.CharField( max_length=100)
    close = models.CharField( max_length=100)
    volume = models.CharField(max_length=100)
