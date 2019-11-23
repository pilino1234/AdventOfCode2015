import json
from typing import Union, Dict, List


def sum_all_numbers(json_str: Union[List, Dict], skip_red: bool = False) -> int:
    total_sum = 0

    if isinstance(json_str, dict):
        if skip_red and ('red' in json_str.keys() or 'red' in json_str.values()):
            return 0
        for key in json_str:
            total_sum += sum_all_numbers(key, skip_red = skip_red)
            total_sum += sum_all_numbers(json_str[key], skip_red = skip_red)
    elif isinstance(json_str, int):
        return json_str
    else:
        for sub_json in json_str:
            if isinstance(sub_json, str):
                continue
            total_sum += sum_all_numbers(sub_json, skip_red = skip_red)
    return total_sum


if __name__ == '__main__':
    with open("input.txt") as file:
        data = json.loads(file.readline().strip())

    assert sum_all_numbers(json.loads('[1,2,3]')) == 6
    assert sum_all_numbers(json.loads('{"a":2,"b":4}')) == 6
    assert sum_all_numbers(json.loads('[[[3]]]')) == 3
    assert sum_all_numbers(json.loads('{"a":{"b":4},"c":-1}')) == 3
    assert sum_all_numbers(json.loads('{"a":[-1,1]}')) == 0
    assert sum_all_numbers(json.loads('[-1,{"a":1}]')) == 0
    assert sum_all_numbers(json.loads('[]')) == 0
    assert sum_all_numbers(json.loads('{}')) == 0

    assert sum_all_numbers(json.loads('[1,2,3]'), skip_red = True) == 6
    assert sum_all_numbers(json.loads('[1,{"c":"red","b":2},3]'), skip_red = True) == 4
    assert sum_all_numbers(json.loads('{"d":"red","e":[1,2,3,4],"f":5}'), skip_red = True) == 0
    assert sum_all_numbers(json.loads('[1,"red",5]'), skip_red = True) == 6

    print(sum_all_numbers(data))
    print(sum_all_numbers(data, skip_red = True))
