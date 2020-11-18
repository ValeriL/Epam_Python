from typing import Any, List

from homework3.task3 import make_filter, sample_data

import pytest


@pytest.mark.parametrize(
    ["filter_data", "expected_result"],
    [
        ({"name": "polly", "type": "bird"}, [sample_data[1]]),
        ({"name": "polly"}, [sample_data[1]]),
        ({"name": "Bill", "type": "person"}, [sample_data[0]]),
        ({"name": "Valeri"}, []),
    ],
)
def test_make_filter_faulty_tests(filter_data, expected_result: List[Any]):
    actual_result = make_filter(**filter_data).apply(sample_data)

    assert actual_result == expected_result
