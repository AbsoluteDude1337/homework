from src.widget import get_date, mask_account_card

def test_get_date():
    assert get_date('2004-02-01') == "01.02.2004"


def test_mask_account_card():
    assert mask_account_card('1234567810111213') == '1234 56** **** 1213'
