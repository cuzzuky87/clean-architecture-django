from django.utils import timezone

class TaskStatus(Enum):
    Undone = 0
    Done = 1

class Task:
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
        


