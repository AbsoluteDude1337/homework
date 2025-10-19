from src.widget import get_date


def test_get_date():
    assert get_date(01022004) == "ДД.ММ.ГГГГ"


def test_mask_account_card():
    assert get_mask_account_card() == ''
