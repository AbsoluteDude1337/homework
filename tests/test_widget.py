from src.widget import get_date, mask_account_card
import pytest
@pytest.fixture
def zalupa():
    return '2005-02-01'

def test_get_date(zalupa):
    data = zalupa
    assert get_date(data) == "01.02.2005"

@pytest.fixture
def zalupa_1():
    return '1234567810111313'

def test_mask_account_card(zalupa_1):
    data = zalupa_1
    assert mask_account_card(data) == '1234 56** **** 1313'

@pytest.fixture
def zalupa_2():
    return 'Счёт 1234567810111313'

def test_mask_account_card_2(zalupa_2):
    data = zalupa_2
    assert mask_account_card(data) == '1234 56** **** 1313'

