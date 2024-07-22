from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number("1234123412341234") == "1234 12** **** 1234"
    assert get_mask_card_number("") == ""
    assert get_mask_card_number("12341234123412") == "1234 12** **34 12"
    assert get_mask_card_number("123412341234123412") == "1234 12** **** **34 12"


def test_get_mask_account():
    assert get_mask_account("") == ""
    assert get_mask_account("0123456789012345678") == "**5678"
    assert get_mask_account("01234567") == "**4567"
