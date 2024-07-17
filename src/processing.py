def filter_by_state(list_of_dicts: list, state: str = "EXECUTED") -> list:
    """Выводит список словарей с определённым значением ключа state"""
    new_list_of_dicts = []
    for item in list_of_dicts:
        for key in item:
            if key == "state" and item[key] == state:
                new_list_of_dicts.append(item)
    return new_list_of_dicts


def sort_by_date(list_of_dicts: list, reverse: bool = True) -> list:
    """Сортировка списка словарей по дате"""
    if reverse:
        sorted_list_of_dicts = sorted(list_of_dicts, key=lambda dicts: dicts["date"], reverse=True)
    else:
        sorted_list_of_dicts = sorted(list_of_dicts, key=lambda dicts: dicts["date"])
    return sorted_list_of_dicts
