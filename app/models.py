from django.db import models
from django.db.models.fields import AutoField

# Create your models here.
class Para(models.Model):
    para_id = models.AutoField(primary_key=True);
    content = models.TextField();
    previous = models.OneToOneField('self', on_delete=models.SET_NULL, null=True, blank=True, related_name="next");

    def __str__(self) -> str:
        return self.content;
