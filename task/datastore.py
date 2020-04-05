from .models import Task as ORMTask
from .entities import Task


class EntityDoesNotExist(Exception):
    pass

class TaskDBRepository:

    def get_find_by_id(self,id):
        try:
            orm_task = ORMTask.objects.get(id = id)
        except ORMTask.DoesNotExist as e:
            raise EntityDoesNotExist
        return self.decode_orm_ticket(orm_task)
    
    def get_find_all(self):
        try:
            orm_tasks = ORMTask.objects.all()
        except ORMTask.DoesNotExist as e:
            raise EntityDoesNotExist
        return self.decode_orm_task(orm_tasks)
    
    def decode_orm_task(self, orm_task_queryset):
        task = Task(
            name=orm_task_queryset.name,
            due_date=str(orm_task_queryset.due_date.strftime('%Y/%m/%d')),
            task_status=orm_task_queryset.task_status,
            postpone_count=orm_task_queryset.postpone_count
        )
        return [task,]

    def decode_orm_task(self,orm_task_queryset):
        tasks = []

        for orm_ticket in orm_task_queryset:
            t = Task(
                name=orm_task_queryset.name,
                due_date=str(orm_task_queryset.due_date.strftime('%Y/%m/%d')),
                task_status=orm_task_queryset.task_status,
                postpone_count=orm_task_queryset.postpone_count
            )
            tasks.append(t)
        
        return tasks
 
        