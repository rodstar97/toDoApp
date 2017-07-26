import logging
import datetime


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
        self._name = name
        self._priority = priority
        self.description = description
        self.status = status
        self.creation_date = self.create_time_stamp()
        self.modified_date = 0
        logger.info('Instance of type {0} created'.format(type(self)))
        logger.info('Attributes are {0}'.format(self.__dict__))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val
        self.set_modified_time()

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
        self.create_time_stamp()
        logger.info('Instance of type {0} with name {1}, Priorty was set to {2}'.format(type(self), self.name, self._priority))

    def create_time_stamp(self):
        return str(datetime.datetime.utcnow())

    def set_modified_time(self):
        self.modified_date = self.create_time_stamp()
