from typing import Optional
import validators
from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys

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

def get_urls(file_path: str) -> Optional[list]:
    with open(file_path, "r") as file:
        return file.readlines()

if __name__ == "__main__":
    if(len(sys.argv) == 1):
        show_help_menu()
        raise Exception("At least one argument must be provided") 
    else:
        sys.argv.pop(0)
        files = []
        gotAllFiles : bool= False 
        urls : Optional[list] = None
        file : Optional[str] = None
        while(sys.argv and not gotAllFiles):
            match sys.argv.pop(0):
                case "--":
                    gotAllFiles= True
                case fileOrUrl:
                    if validators.url(fileOrUrl) and file ==None:
                        if urls == None:
                            urls = []
                        urls.append(fileOrUrl)
                    elif urls == None and file == None:
                        file = fileOrUrl
                    else:
                        show_help_menu()
                        raise Exception("either a file must be provided or one or more urls")
        if(file != None):
            urls = get_urls(file)
        
        print(urls)

        while(sys.argv):
            pass
        