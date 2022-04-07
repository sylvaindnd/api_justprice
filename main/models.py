from asyncio.unix_events import DefaultEventLoopPolicy
from django.db import models

class Object(models.Model):
    used = models.BooleanField(default=False)
    image = models.CharField(max_length=512, default="", blank=True)
    name = models.CharField(max_length=128, default="", blank=True)
    description = models.CharField(max_length=256, default="", blank=True)
    price = models.FloatField(default=0)
    price_before = models.IntegerField(default=0)
    price_after = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.price_before = int(str(self.price).split('.')[0])
        self.price_after = int(str(self.price).split('.')[1])
        super().save(*args, **kwargs)
