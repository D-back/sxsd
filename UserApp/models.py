from django.db import models

# Create your models here.
class SxsdUser(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=128)
    head = models.ImageField(upload_to='head')
    active = models.BooleanField(default=False)
    token = models.CharField(max_length=256)

    class Meta:
        db_table = 'sxsd_user'