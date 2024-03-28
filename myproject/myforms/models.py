from django.db import models

# Create your models here.
class FormData(models.Model):
  name = models.CharField(max_length = 100)
  phone = models.IntegerField(blank=True, null=True)
  class Meta:
        db_table="Persons"