import uuid
from django.db import models

class Task(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=150)
    due_date = models.DateField()
    TASK_STATUS = [
        (0,"UNDONE"),
        (1,"DONE")
    ]
    task_status = models.IntegerField(choices=TASK_STATUS)
    postpone_count = models.IntegerField()
