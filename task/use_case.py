from .entities import Task
from .repository import TaskRepository


class TaskUseCase:
    @classmethod
    def postpone_task(cls,id):
        task = TaskRepository.get_task_by_id(id)
        task.postpone()
        #TaskRepository.save(task)