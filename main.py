import utils
from typing import Optional
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen


if __name__ == "__main__":
    if (len(sys.argv) == 1):
        utils.display_menu_and_throw_exception("At least one argument must be provided")
    else:
        sys.argv.pop(0)
        files = []

        (urls, file) = utils.read_required_arguments(sys.argv)

        if (file != None):
            urls = utils.get_urls(file)
        (hours, days) = utils.read_optional_argument(sys.argv)
