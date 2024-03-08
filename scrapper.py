
from typing import Optional
from bs4 import BeautifulSoup
from urllib.request import urlopen
import mechanicalsoup
from functools import reduce


def scrap(url: str) -> list[str]:
    browser = mechanicalsoup.StatefulBrowser()
    browser.set_user_agent('Mozilla/5.0')
    page = browser.get(url)
    links_to_location = page.soup.select("a[href*=\/huur\/]")
    appartments = map((lambda href: href["href"] ),links_to_location)
    unique_elements = reduce(lambda uniqueUrls, newUrl: uniqueUrls +
                             [newUrl] if newUrl not in uniqueUrls else uniqueUrls, appartments, [])
    print(unique_elements)

    return []
