import sys
import validators
from typing import Optional


HELP_MENU = """

         usage: python3 main.py args -- [options]
         where args is either: a path to a file containing a list of urls, or one or more urls to scrape from.
         The resulting list of appartments will be written to appartments.txt
         urls must be stored one per line;
         Options:
                 --days d              How many days back to look for new posts.
                 --hours h             How many hours back to look for new posts.
                 --help                show this menu
 """


def show_help_menu() -> None:
    print(HELP_MENU)


def display_menu_and_throw_exception(msg: str):
    show_help_menu()
    raise Exception(msg)


def get_urls(file_path: str) -> Optional[list]:
    with open(file_path, "r") as file:
        return file.readlines()

# returns the urls passed passed as parameter or the file containing urls


def read_required_arguments(arguments: list) -> tuple[Optional[list], Optional[str]]:
    gotAllFiles: bool = False
    urls: Optional[list] = None
    file: Optional[str] = None
    while (arguments and not gotAllFiles):
        match arguments.pop(0):
            case "--":
                gotAllFiles = True
            case fileOrUrl:
                if validators.url(fileOrUrl) and file == None:
                    if urls == None:
                        urls = []
                    urls.append(fileOrUrl)
                elif urls == None and file == None:
                    file = fileOrUrl
                else:
                    show_help_menu()
                    display_menu_and_throw_exception(
                        "either a file must be provided or one or more urls")
    return (urls, file)


def get_number(arguments: list) -> int:
    if (not arguments):
        display_menu_and_throw_exception("Expected a number, found nothing.")
    number = arguments.pop(0)
    if not number.isnumeric():
        display_menu_and_throw_exception(
            f"Expected an integer, found {number}")
    return int(number)

# returns optional arguments if any given. (days, hours)


def read_optional_argument(arguments: list) -> tuple[Optional[int], Optional[int]]:
    days: Optional[int] = None
    hours: Optional[int] = None

    while (arguments and not days and not hours):
        match arguments.pop(0):
            case "--days":
                days = get_number(arguments)
            case "--hours":
                hours = get_number(arguments)
            case badArgument:
                show_help_menu()
                display_menu_and_throw_exception(
                    f"Uknown optinal argument found: {badArgument}.")

    if hours:
        daysToAdd = hours / 24
        hours = hours % 24
        if days == None:
            days = 0
        days += daysToAdd
    
    if hours == None or (hours == 0 and days == None):
    # if no days or hours set, we just check 8 hours in the past
        hours = 8
    return (days, hours)
