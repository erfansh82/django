from faulthandler import is_enabled
from django.db import models


class post(models.Model):
   title=models.CharField(max_length=50)
   text=models.TextField()
   is_enable=models.BooleanField(default=False)
   publish_date=models.DateField()
   created_time=models.DateField()
   updated_time=models.DateField()