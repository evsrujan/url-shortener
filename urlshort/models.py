from django.db import models

# Create your models here.
class makeurl(models.Model):
    longurl = models.CharField(max_length=300)
    shorturl = models.CharField(max_length=300)
    count = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.shorturl
    