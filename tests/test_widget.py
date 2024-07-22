import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "number, mask",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("", ""),
    ],
)
def test_mask_account_card(number, mask):
    assert mask_account_card(number) == mask


def test_get_date(date_to_formate):
    assert get_date(date_to_formate) == "11.03.2024"
