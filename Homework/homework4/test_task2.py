import urllib
from unittest.mock import MagicMock
from urllib.error import HTTPError

from homework4.task2 import count_dots_on_i

import pytest


def test_count_dots_on_i(monkeypatch):
    monkeypatch.setattr(
        urllib.request,
        "urlopen",
        MagicMock(
            return_value=[
                b"<html>",
                b"<head>hii</head>",
                b"<body>hiii</body>",
                b"/html",
            ]
        ),
    )
    assert count_dots_on_i("https://example.com/") == 5


def test_value_error_raise_http_error(monkeypatch):
    monkeypatch.setattr(
        urllib.request,
        "urlopen",
        MagicMock(side_effect=HTTPError(404, "NF", "", "", "")),
    )
    with pytest.raises(ValueError, match="Unreachable https://notfound"):
        count_dots_on_i("https://notfound")
