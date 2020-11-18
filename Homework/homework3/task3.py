from typing import Any, List, Mapping


class Filter:
    """
    Helper filter class.

    Accepts a list of single-argument unctions that
    return True if object in list conforms to some criteria.
    """

    def __init__(self, functions):
        self.functions = functions

    def apply(self, data: Mapping[Any, Any]) -> List[Any]:
        return [item for item in data if all(i(item) for i in self.functions)]


def make_filter(**keywords: Any):
    """Generate filter object for specified keywords."""
    filter_funcs = []
    for key, value in keywords.items():

        def keyword_filter_func(data: Mapping[Any, Any]) -> bool:
            return data[key] == value

        filter_funcs.append(keyword_filter_func)
    return Filter(filter_funcs)


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]
