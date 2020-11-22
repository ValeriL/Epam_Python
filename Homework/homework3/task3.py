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


def make_filter(**keywords: Any) -> Filter:
    """Generate filter object for specified keywords."""
    filter_funcs = []
    for key, value in keywords.items():

        def inner(key: Any, value: Any):
            def keyword_filter_func(data: Mapping[Any, Any]) -> bool:
                return key in data and data[key] == value

            return keyword_filter_func

        filter_funcs.append(inner(key, value))
    return Filter(filter_funcs)
