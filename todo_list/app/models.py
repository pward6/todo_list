from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    notes = models.CharField(max_length=1000, null=True, blank=True)
    goal = models.DateTimeField(null=True)


    def __str__(self):
        return self.task