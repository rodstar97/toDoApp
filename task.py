import logging
logger = logging.getLogger(__name__)

class Task(object):
    """ Task Object hold all Attributes for ToDo Task

    Args:
        priority: int 0 to 100
        name: string name of the task
        description: multiline string with links
        status: string (should be one from _settings.json file)
    """
    def __init__(self, name='task', priority=0, description='describe task', status='toDo'):
        self.name = name
        self._priority = priority
        self.description = description
        self.status = status
        logger.info('Instance of type {0} created'.format(type(self)))
        logger.info('Attributes are {0}'.format(self.__dict__))

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, val):
        if val > 100:
            self._priority = 100
        elif val < 0:
            self._priority = 0
        else:
            self._priority = val
        logger.info('Instance of type {0} with name {1}, Priorty was set to {2}'.format(type(self), self.name, self._priority))

