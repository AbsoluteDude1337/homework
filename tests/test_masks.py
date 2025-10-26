from src.masks import get_mask_card_number
import pytest
@pytest.fixture
def zalupa():
    return 1234567810111231

def test_get_mask_card_number(zalupa):
    data = zalupa
    assert get_mask_card_number(data) == '1234 56** **** 1231'


from src.masks import get_mask_account

@pytest.fixture
def zalupa_1():
    return 12345678910111213141
def test_get_mask_account(zalupa_1):
    data = zalupa_1
    assert get_mask_account(data) == '**3141'
