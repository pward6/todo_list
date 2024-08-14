from django.db import models

# Create your models here.
class Item(models.Model):
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.task