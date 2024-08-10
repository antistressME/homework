import json
import logging
import os

from src.external_api import currency_conversion

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name): %(levelname)s: %(message)s",
    filename="logs/utils.log",
    filemode="w",
)
logger = logging.getLogger("utils")


def get_list(file_json: str) -> list[dict]:
    """Преобразуем json файл в список словарей"""
    transact_list = []
    logger.info("Получаем путь к файлу...")
    path = os.path.dirname(__file__)[:-4]
    way_to_file = os.path.join(path, "data", file_json)
    try:
        logger.info(f"Открываем файл {file_json}...")
        with open(way_to_file, "r", encoding="UTF8") as file:
            transaction = json.load(file)
            if type(transaction) == list:
                transact_list = transaction
                logger.info(f"Данные из файла {file_json} успешно получены")
        return transact_list
    except Exception as ex:
        logger.error(f"Произошла ошибка чтения файла: {ex}")


def get_amount(operation: dict) -> float:
    """Рассчитываем сумму транзакции в рублях"""
    amount = operation["operationAmount"]["amount"]
    currency = operation["operationAmount"]["currency"]["code"]
    if currency != "RUB":
        amount = currency_conversion(amount, currency)
    return float(amount)
