def filter_by_state(list_of_dicts: list, state: str = "EXECUTED") -> list:
    """Выводит список словарей с определённым значением ключа state"""
    new_list_of_dicts = []
    for item in list_of_dicts:
        for key in item:
            if key == "state" and item[key] == state:
                new_list_of_dicts.append(item)
    return new_list_of_dicts

