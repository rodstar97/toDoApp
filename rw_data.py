import json, codecs



def write_json_file(data):
    '''Write Json to Disk

    Args:
        data: Json string


    toDO: test if Json string is Valid
          test if file open
    '''
    with open('data/data.json', 'wb') as f:
        json.dump(data, codecs.getwriter('utf-8')(f), ensure_ascii=False)


