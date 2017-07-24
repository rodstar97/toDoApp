class Task():
    ''' Task Object hold all Attributes for ToDo Task

    Args:
        priority: int 0 to 100
        name: string name of the task
        description: multiline string with links
        status: string (should be one from _settings.json file)


    '''
    def __init__(self, priority=0, name = 'task', description = 'describe task', status = 'toDo'):
        self._priority =  priority
        self.name = name
        self.description = description
        self. status = status

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority_setter(self, val):
        if val > 100:
            self._priority = 100
        elif val < 0:
            self._priority = 0
        else:
            self._priority = val

