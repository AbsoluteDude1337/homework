from src.processing import filter_by_state


def test_filter_by_state():
    assert filter_by_state() == ''


from src.processing import sort_by_date


def test_sort_by_date():
    assert sort_by_date() == ""
