import re

from src.utils import get_list
from collections import Counter
from collections import defaultdict

def filter_by_str(operations: list[dict], search_str: str) -> list:
    """Получение списка словарей, у которых в описании указанная строка."""
    pattern = r'description\W\W\s\W' + search_str
    filtered_operations = []
    for operation in operations:
        if re.search(pattern, str(operation)):
            filtered_operations.append(operation)
    return filtered_operations


if __name__ == "__main__":
    search_str = "Открытие вклада"
    operations = get_list("operations.json")
    print(filter_by_str(operations, search_str))


def filter_by_description(operations: list[dict], description: list) -> dict:
    """Получение соваря категорий и количества операций в каждой категории."""
    result = defaultdict(int)
    for item in description:
        result[item]
        counted = Counter(re.findall(item, str(operations)))
        result.update(counted)
    return result


if __name__ == "__main__":
    operations = get_list("operations.json")
    description = ["Перевод организации", "Перевод со счета на счет", "test"]
    print(filter_by_description(operations, description))
