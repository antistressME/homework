from masks import get_mask_account
from masks import get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Максировка номера счёта или номера карты"""
    if "сч" in account_card.lower():
        return get_mask_account(account_card)
    else:
        return get_mask_card_number(account_card)


print(mask_account_card("Visa Platinum 7000792289606361"))
