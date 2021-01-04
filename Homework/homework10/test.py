import json

import asynctest as asynctest

from bs4 import BeautifulSoup

from homework10.task import (
    fetch_html,
    get_companies_urls_and_growth,
    get_company_code,
    get_company_name,
    get_low_high,
    get_pe_ratio,
    get_profit,
    get_stock_price,
    write_json,
)

import pytest


def test_write_json():
    data = [
        {"code": "code1", "name": "name1", "key": 2},
        {"code": "code2", "name": "name2", "key": 3},
        {"code": "code3", "name": "name3", "key": 1},
    ]
    key = "key"
    write_json(key, data)
    with open("Homework/homework10/top_10_key.json", "r") as f:
        assert json.load(f) == [
            {"code": "code2", "name": "name2", "key": 3},
            {"code": "code1", "name": "name1", "key": 2},
            {"code": "code3", "name": "name3", "key": 1},
        ]


def test_company_data_getters(monkeypatch):
    import homework10.task

    with open("Homework/homework10/example_company_page.html", "r") as f:
        soup = BeautifulSoup(f.read(), "lxml")

    def mock_current_currency():
        return 100

    monkeypatch.setattr(homework10.task, "get_current_currency", mock_current_currency)

    assert get_company_name(soup) == "Tesla"
    assert get_company_code(soup) == "TSLA"
    assert get_pe_ratio(soup) == 14392.16
    assert get_low_high(soup) == (70.102, 718.72)
    assert get_profit((1, 2)) == 100
    assert get_stock_price(soup) == 72372.0


@pytest.mark.asyncio
async def test_get_companies_urls_and_growth(monkeypatch):
    import homework10.task

    def mock_fetch_html(path):
        with open(path, "r") as f:
            return f.read()

    async_mock_fetch_html = asynctest.CoroutineMock(
        fetch_html, side_effect=mock_fetch_html
    )
    monkeypatch.setattr(homework10.task, "fetch_html", async_mock_fetch_html)
    url = "Homework/homework10/example_first_page.html"
    companies_urls_and_growth = await get_companies_urls_and_growth(url)

    assert companies_urls_and_growth == [
        {"href": "/stocks/mmm-stock", "growth": -1.31},
        {"href": "/stocks/aos-stock", "growth": 14.84},
    ]
