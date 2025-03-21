from django.db import models

class StockData(models.Model):
    timestamp = models.DateTimeField()
    open_price = models.FloatField()
    close_price = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()

    def __str__(self):
        return f"{self.timestamp} - {self.close_price}"

