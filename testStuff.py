from task import Task
import logging
import json
from rw_data import write_json_file

def testStuff():
    objectlist = []
    for i in range(19):
        a = Task(name='{0}'.format(i))
        objectlist.append(a)


    json_string = json.dumps([ob.__dict__ for ob in objectlist])

    write_json_file(json_string)

    a = Task(name='te55st')

    a.priority=1001
    logging.info(a.priority)


