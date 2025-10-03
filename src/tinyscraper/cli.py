# Imports
from .api import scrape_thread_to_json


def main():
    url = input("url:\n")
    site_name = input("site name:\n")
    scrape_thread_to_json(url, site_name=site_name)


if __name__ == '__main__':
    main()