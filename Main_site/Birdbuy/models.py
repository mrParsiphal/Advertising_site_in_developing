from django.db import models
from django.contrib import admin

class Birds(models.Model):
    breed = models.CharField(max_length=20)
    price = models.IntegerField(null=True)
    image = models.TextField(blank=True)

    def __str__(self):
        return self.breed

    class Meta:
        verbose_name_plural = 'Birds'


class Content(models.Model):
    number_phone = models.CharField(max_length=16)
    cart_sum_enable = models.BooleanField()
    cart_sum = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Content'

admin.site.register(Birds)
admin.site.register(Content)


