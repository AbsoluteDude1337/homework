from src.widget import get_date


def test_get_date():
    assert get_get_date(01.02.2004) == 'ДД.ММ.ГГГГ'