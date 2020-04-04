"""

"""

class TaskRepository:
    def __init__(self,db_repo):
        self.__db_repo = db_repo
    
    def get_task_by_id(self,id):
        task = self.__db_repo.get_find_by_id(id = id)
        return task
    
    def get_tasks(self):
        tasks = self.__db_repo.get_all()
        return tasks
