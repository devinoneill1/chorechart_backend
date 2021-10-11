from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Task(models.Model):
    task_name = models.TextField
    task_day = models.DateField("day of the week repeating",blank=True)
    repeat = models.BooleanField
    priority = models.PositiveIntegerField(
        default=10,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
            ]
        )
    status = models.ForeignKey(
        'Status',
        on_delete=models.CASCADE
    )    


class Status(models.Model):
    status_name = models.CharField(max_length=200)