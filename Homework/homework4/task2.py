"""
Write a function that accepts an URL as input.

Count how many letters `i` are present in the HTML by this URL.
Write a test that check that your function works.
Test should use Mock instead of real network interactions.
You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests
>>> count_dots_on_i("https://example.com/")
59
"""
import urllib.request
from urllib.error import URLError


def count_dots_on_i(url: str) -> int:
    try:
        return sum(
            sum(1 for char in line.decode() if char == "i")
            for line in urllib.request.urlopen(url)  # noqa : S310
        )
    except URLError as e:
        raise ValueError(f"Unreachable {url}", e)
