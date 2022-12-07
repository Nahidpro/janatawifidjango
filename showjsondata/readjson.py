import json


def read_json_file(path):
    file = open(path, "r")
    data = file.read()
    finaldata = json.loads(data)
    limited_json_data =finaldata[1:20]
    file.close()
    
    return limited_json_data