import re

from src.utils import get_list


def filter_by_str(operations: list[dict], search_str: str) -> list:
    """Получение списка словарей, у которых в описании указанная строка."""
    filtered_operations = []
    for operation in operations:
        if re.search(search_str, str(operation)):
            filtered_operations.append(operation)
    return filtered_operations


if __name__ == "__main__":
    search_str = "Открытие вклада"
    operations = get_list("operations.json")
    print(filter_by_str(operations, search_str))


def filter_dy_description(operations: list[dict], description: list) -> dict:
    """Получение соваря категорий и количества операций в каждой категории."""
    result = {}
    for item in description:
        descriptions = re.findall(item, str(operations))
        result[item] = len(descriptions)
    return result


if __name__ == "__main__":
    operations = get_list("operations.json")
    description = ["Перевод организации", "Перевод со счета на счет"]
    print(filter_dy_description(operations, description))
