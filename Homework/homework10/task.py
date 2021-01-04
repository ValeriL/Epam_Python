import asyncio
import json
import re
from datetime import datetime
from typing import Dict, List, Tuple

import aiohttp

from bs4 import BeautifulSoup

import requests


def get_company_name(soup) -> str:
    """Get company name from the page."""
    return soup.find("span", {"class": "price-section__label"}).text.strip()


def get_company_code(soup) -> str:
    """Get company name from the page."""
    return (
        soup.find("div", {"class": "price-section__row"})
        .find("span", {"class": "price-section__category"})
        .find("span")
        .text[2:]
    )


def get_stock_price(soup) -> float:
    """Get stock price in usd from the page."""
    stock_price_usd = soup.find("span", {"class": "price-section__current-value"}).text
    return round(float(stock_price_usd.replace(",", "")) * get_current_currency(), 2)


def get_pe_ratio(soup) -> float:
    """Get P/E ratio from the page."""
    try:
        return float(
            soup.find("div", string=re.compile("P/E Ratio")).previous_sibling.replace(
                ",", ""
            )
        )
    except AttributeError:
        return 0


def get_low_high(soup) -> Tuple[float, float]:
    """Get 52 Week Low and 52 Week High values from the page."""
    script = soup.find("div", {"class": "snapshot"}).find("script")
    low = float(re.search(r"low52weeks: (\d*\.\d+|\d+),", script.string).group(1))
    high = float(re.search(r"high52weeks: (\d*\.\d+|\d+),", script.string).group(1))
    return low, high


def get_profit(low_high_values: Tuple[float, float]) -> float:
    """Get a value of profit if we buy the stock at 52 Week Low price and sell at 52 Week High price."""
    low, high = low_high_values
    return round((high - low) / low * 100, 2)


def sort_by_key(data: List[Dict], value: str) -> List[Dict]:
    """Sort the company info by given key value."""
    return sorted(data, key=lambda x: x[value], reverse=True)[0:10]


def get_current_currency() -> float:
    """Get today currency from the bank page."""
    current_datetime = datetime.now()
    year = current_datetime.year
    month = current_datetime.month
    formatted_month = month if len(str(month)) > 1 else "0" + str(month)
    day = current_datetime.day
    formatted_day = day if len(str(day)) > 1 else "0" + str(day)
    bank_url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={formatted_day}/{formatted_month}/{year}"
    page = requests.get(bank_url)
    soup = BeautifulSoup(page.text, "lxml")
    currency = (
        soup.find("valute", {"id": "R01235"}).find("value").text.replace(",", ".")
    )
    return float(currency)


async def fetch_html(url: str) -> str:
    """Fetch the text from any page."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def get_company_data(company: List) -> Dict:
    """Get the information about the company."""
    url = "https://markets.businessinsider.com" + company["href"]
    soup = BeautifulSoup(await fetch_html(url), "lxml")
    return {
        "name": get_company_name(soup),
        "code": get_company_code(soup),
        "price": get_stock_price(soup),
        "pe_ratio": get_pe_ratio(soup),
        "growth": company["growth"],
        "profit": get_profit(get_low_high(soup)),
    }


async def get_companies_urls_and_growth(url: str) -> List[Dict]:
    """Get the links of companies' pages and 1 year growth/fall value in percents from one page."""
    companies = []
    soup = BeautifulSoup(await fetch_html(url), "lxml")
    for company_row in soup.find_all("tr")[2:]:
        href = company_row.find_all("td")[0].a["href"]
        growth = company_row.find_all("td")[9].text.split()[1]
        companies.append({"href": href, "growth": float(growth.replace("%", ""))})
    return companies


async def get_pages_companies() -> List[List]:
    """Get the companies' links and 1 year growth/fall value from all pages."""
    url = "https://markets.businessinsider.com/index/components/s&p_500?p="
    tasks = [get_companies_urls_and_growth(url + str(num)) for num in range(1, 11)]
    return await asyncio.gather(*tasks)


async def get_companies_data() -> List[Dict]:
    """Get the information about all companies on all pages of the site."""
    pages = await get_pages_companies()
    tasks = [get_company_data(company) for page in pages for company in page]
    return await asyncio.gather(*tasks)


def write_json(key: str, data: List[Dict]) -> None:
    """Write the selected and formatted information about companies into json file."""
    sorted_data = sort_by_key(data, key)
    top_data = []
    for company in sorted_data:
        top_data.append(
            {"code": company["code"], "name": company["name"], f"{key}": company[key]}
        )
    with open("top_10_" + key + ".json", "w+") as f:
        json.dump(top_data, f)


if __name__ == "__main__":
    companies_data = asyncio.run(get_companies_data())
    keys = ["price", "pe_ratio", "profit", "growth"]
    for key in keys:
        write_json(key, companies_data)
