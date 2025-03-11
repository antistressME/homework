import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Максировка номера счёта или номера карты"""
    if "сч" in account_card.lower():
        return account_card[:5] + get_mask_account(account_card)
    else:
        card_number_dig = ""
        payment_system = ""
        for item in account_card:
            if item.isdigit():
                card_number_dig += item
            else:
                payment_system += item
    return payment_system + get_mask_card_number(card_number_dig)


def get_date(date: str) -> str:
    """Изменение формата даты"""
    format_data = datetime.datetime.fromisoformat(date)
    new_format_data = format_data.strftime("%d.%m.%Y")
    return new_format_data
