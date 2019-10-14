from django.db import models
from cvat.apps.engine.models import Task

# Create your models here.

class Instruction(models.Model):
    task_id = models.OneToOneField(Task,primary_key="True",on_delete=models.CASCADE)
    instruction_text = models.CharField(null="True",max_length=256)

    def __str__(self):
        return self.instruction_text