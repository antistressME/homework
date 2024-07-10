def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    return str(card_number)[0:4] + " " + str(card_number)[4:6] + "** **** " + str(card_number)[-4:]


def get_mask_account(account_number: int) -> str:
    """Функция получения маски номера счёта"""
    return "**" + str(account_number)[-4:]
