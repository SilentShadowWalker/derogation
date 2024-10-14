from django.db import models

# Create your models here.
class City(models.Model):
    code = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=30)

    class Meta:
        managed = False  # Use the existing table without altering it
        db_table = 'wilaya'  # Use this specific table name