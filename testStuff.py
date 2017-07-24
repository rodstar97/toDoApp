from task import Task
import json
from rw_data import write_json_file

objectlist = []
for i in range(19):
    a = Task(name='{0}'.format(i))
    objectlist.append(a)


json_string = json.dumps([ob.__dict__ for ob in objectlist])

#write_json_file(json_string)

a = Task(name='test')
a.priority_setter = 101
print a._priority