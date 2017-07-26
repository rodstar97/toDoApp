import json, codecs
import logging
logger = logging.getLogger(__name__)


def write_json_file(list_of_objs):
    '''Write Json to Disk

    Args:
        list_of_objs: List of Task objs


    toDO: test if Json string is Valid
          test if file open
    '''

    try:
        json_string = json.dumps([ob.__dict__ for ob in list_of_objs])
        with open('data/data.json', 'wb') as f:
            json.dump(json_string, codecs.getwriter('utf-8')(f), ensure_ascii=False)

    except Exception as e:
        logger.exception(" failed to write data to Json", exc_info=1)




def read_json_file():
    try:
        data = 0
        with open('data/data.json') as data_file:
            data = json.load(data_file)
        return data
    except Exception as e:
        logger.exception(" failed to read data from Json", exc_info=1)