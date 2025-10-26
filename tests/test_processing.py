from src.processing import filter_by_state
import pytest
@pytest.fixture
def zalupa():
    return [{}]

def test_filter_by_state(zalupa):
    data = zalupa
    assert filter_by_state(data) == []


from src.processing import sort_by_date

@pytest.mark.parametrize("a,b",[([{'date': '2002-10-10'}],[{'date': '2002-10-10'}])])

def test_sort_by_date(a,b):
    assert sort_by_date(a) == b
