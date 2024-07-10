from masks.py import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Максировка номера счёта или номера карты"""
    if "сч" in account_card.lower():
        return get_mask_account(account_card)
    else:
        return get_mask_card_number(account_card)


def get_date(date: str) -> str:
    """Изменение формата даты"""
    new_format_data = date[8:10] + "." + date[5:7] + "." + date[:4]
    return new_format_data
