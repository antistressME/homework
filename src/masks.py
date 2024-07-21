def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""

    stars_points = len(card_number) - 10
    mask_card_number = card_number[:6] + "*" * stars_points + card_number[-4:]
    count = 0
    mask_card = ""
    for digit in mask_card_number:
        if count != 0 and count % 4 == 0:
            mask_card += " "
        count += 1
        mask_card += digit
    return mask_card



def get_mask_account(account_number: str) -> str:
    """Функция получения маски номера счёта"""
    return "**" + account_number[-4:]

