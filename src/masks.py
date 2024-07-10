def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    card_number_dig = ""
    payment_system = ""
    for item in card_number:
        if item.isdigit():
            card_number_dig += item
        else:
            payment_system += item
    mask_card_number = card_number_dig[0:4] + " " + card_number_dig[4:6] + "** **** " + card_number_dig[-4:]
    return payment_system + mask_card_number


def get_mask_account(account_number: str) -> str:
    """Функция получения маски номера счёта"""
    return account_number[0:5] + "**" + account_number[-4:]
