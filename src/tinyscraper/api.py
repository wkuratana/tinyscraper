# Imports
import datetime
import logging
import os
from enum import Enum
from scrapy.crawler import CrawlerProcess
from .spiders.tinyboard import TinyboardSpider


class FileExtension(str, Enum):
    json = 'json'
    jsonl = 'jsonl'
    csv = 'csv'
    xml = 'xml'

# TODO: Optimize code reuse, add logging
def scrape_thread_to_json(url: str, site_name = None):
    """
    Scrape a thread URL and write out to a JSON file.
    The file is locally written to a `/data` directory.

    Args:
        url (str): URL to a thread page.
        site_name: Suffix for the output file name.
    """
    if site_name is None: site_name = 'tinyboard'

    os.makedirs('data', exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%dT%H%M")

    file_path = os.path.join('data', f'{timestamp}_{site_name}.json')

    process = CrawlerProcess(settings={
        'FEEDS': {
            file_path: {
                'format': 'json', 
                'encoding': 'utf8',
                'indent': 4,
            },
        },
        'LOG_LEVEL': 'INFO',
        'DEPTH_LIMIT': 1  # Make 2 for board/homepage
    })
    process.crawl(TinyboardSpider, start_urls=[url])
    process.start()

# def scrape_board_homepage_to_json(url: str, site_name = None):
#    '''Scrape a board or homepage and write out to a JSON file.'''

# def scrape_thread_to_jsonl(url: str, site_name = None):
#    '''Scrape a thread URL and write out to a JSONL file.'''

# def scrape_board_homepage_to_jsonl(url: str, site_name = None):
#    '''Scrape a board or homepage and write out to a JSONL file.'''

# def scrape_thread_to_csv(url: str, site_name = None):
#    '''Scrape a thread URL and write out to a JSONL file.'''

# def scrape_board_homepage_to_csv(url: str, site_name = None):
#    '''Scrape a board or homepage and write out to a JSONL file.'''

# def scrape_thread_to_xml(url: str, site_name = None):
#    '''Scrape a thread URL and write out to a JSONL file.'''

# def scrape_board_homepage_to_xml(url: str, site_name = None):
#    '''Scrape a board or homepage and write out to a JSONL file.'''
