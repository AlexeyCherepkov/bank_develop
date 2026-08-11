def filter_by_state(data_list:list, key='EXECUTED') -> list:
    result = []
    for i in data_list:
        if i['state'] == key:
            result.append(i)
    return result
