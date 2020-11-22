from homework3.task3 import make_filter


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]


def test_some_key_not_matching_filter_filtered():
    item_filter = make_filter(name="Bill", kind="parrot")
    assert item_filter.apply(sample_data) == []


def test_some_item_not_matching_filter_filtered():
    item_filter = make_filter(name="Bill", last_name="Klinton")
    assert item_filter.apply(sample_data) == []


def test_more_items_filter_filtered():
    item_filter = make_filter(
        name="Bill",
        last_name="Gilbert",
        occupation="was here",
        type="person",
        kind="parrot",
    )
    assert item_filter.apply(sample_data) == []


items = [{"item_key": "Gilbert"}]


def test_empty_list_filtered():
    empty_filter = make_filter()
    assert empty_filter.apply(items) == items


def test_value_not_matching_filter_filtered():
    item_filter = make_filter(item_key="Klinton")
    assert item_filter.apply(items) == []


def test_item_matching_filter_not_filtered():
    item_filter = make_filter(item_key="Gilbert")
    assert item_filter.apply(items) == items


def test_key_not_matching_filter_filtered():
    item_filter = make_filter(filter_key="Gilbert")
    assert item_filter.apply(items) == []
