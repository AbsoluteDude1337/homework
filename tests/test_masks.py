from src.masks import get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number(1234567810111231) == '1234 56** **** 1231'


from src.masks import get_mask_account


def test_get_mask_account():
    assert get_mask_account(12345678910111213141) == '**3141'
