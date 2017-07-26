from task import Task
import logging
import json
import datetime
from rw_json_data import write_json_file, read_json_file
from pprint import pprint



def testStuff():
    objectlist = []


    # create two entries
    task1 = Task(name='task1')
    task2 = Task(name='task2')

    task1.priority=1001
    task2.priority=-6
    objectlist.append(task1)
    objectlist.append(task2)



    write_json_file(task1)
    #print datetime.datetime.utcnow()
    data = read_json_file()
    #print data
    # pprint(data)


testStuff()



