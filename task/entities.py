from django.utils import timezone
import datetime
from typing import Final

class DomainException(Exception):
    pass

class TaskStatus(Enum):
    Undone = 0
    Done = 1


class Task:
    
    __MAX_POSTPONE_COUNT:Final = 3

    def __init__(
        self,
        name,
        due_date,
        task_status = TaskStatus.Undone,
        postpone_count=0,
    ):
        self.name = name
        if timezone.now() > due_date:
            raise ValueError()
        self.due_date = due_date
        self.task_status = task_status
        self.postpone_count = postpone_count
        self.due_date = due_date

    def postpone(self):
        validate_postpone_count()
        self.due_date = self.due_date + datetime.timedelta(days=1)
        self.postpone_count += 1
    
    def validate_postpone_count(self):
        if self.postpone_count >= __MAX_POSTPONE_COUNT:
            raise DomainException("最大延期回数を超えています")
        

        


