import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name): %(levelname)s: %(message)s",
    filename="logs/masks.log",
    filemode="w",
)
logger = logging.getLogger("masks")


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    logger.info("Начало работы программы маскировки номера банковской карты")
    if 0 < len(card_number) <= 10:
        logger.warning("Введите номер карты полностью")
        return "Введите номер карты полностью"
    stars_points = len(card_number) - 10
    mask_card_number = card_number[:6] + "*" * stars_points + card_number[-4:]
    count = 0
    mask_card = ""
    for digit in mask_card_number:
        if count != 0 and count % 4 == 0:
            mask_card += " "
        count += 1
        mask_card += digit
    logger.info(f"Маска карты получена: {mask_card}")
    return mask_card


def get_mask_account(account_number: str) -> str:
    """Функция получения маски номера счёта"""
    logger.info("Начало работы программы маскировки номера счёта")
    if len(account_number) == 0:
        logger.warning("Номер счёта не получен")
        return ""
    mask_account = "**" + account_number[-4:]
    logger.info(f"Маска счёта получена: {mask_account}")
    return mask_account
