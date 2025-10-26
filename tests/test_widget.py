from src.widget import get_date, mask_account_card

def test_get_date():
    assert get_date('2005-02-01') == "01.02.2005"


def test_mask_account_card():
    assert mask_account_card('1234567810111313') == '1234 56** **** 1313'


def test_mask_account_card_2():
    assert mask_account_card('Счёт 1234567810111313') == '1234 56** **** 1313'