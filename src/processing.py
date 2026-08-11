def filter_by_state(data_list:list, key='EXECUTED') -> list:
    result = []
    for i in data_list:
        if i['state'] == key:
            result.append(i)
    return result

def sort_by_date(data_list:list, sort_parameter=True) -> list:
    result = sorted(data_list, key=lambda x: x["date"], reverse=sort_parameter)
    return result
