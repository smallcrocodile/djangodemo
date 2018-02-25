from django.db import models

# Create your models here.
class MyModel(models.Model):
    item = models.CharField(max_length=100)

    def __str__(self):
        return self.item

    class Meta:
        verbose_name = 'MM'

