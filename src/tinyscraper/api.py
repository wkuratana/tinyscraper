# Imports
import datetime
import logging
import os
from scrapy.crawler import CrawlerProcess
from .spiders.tinyboard import TinyboardSpider
from .types import FileExtension

def scrape_from_url(
    url: str,
    filename: str|None,
    filename_suffix: str,
    filename_extension: FileExtension,
    directory: str
):
    """
    Scrape a homepage, catalog page, or a specific thread URL.

    If a specific thread URL is passed, then a single file will be written 
    out. If a homepage or catalog page is passed, then a file for each listed
    thread (formatted as though each thread was passed individually) will
    be written out.

    Args:
        url (str): Absolute URL to a homepage, catalog, or thread.
        filename (str|None): Name of file written out; will be numbered if >1.
        filename_suffix (str): End of default file numbering scheme. See docs.
        filename_extension (FileExtension): File type.
        directory (str): Directory where all files will go after scraping.
    """
    process = CrawlerProcess(settings={
        'LOG_LEVEL': 'INFO',
        'ITEM_PIPELINES': {
            'tinyscraper.pipelines.PerItemFilePipeline': 300,
            # Add formatting pipeline down the line
        }
    })
    process.crawl(
        TinyboardSpider, 
        start_urls=[url],
        filename=filename,
        filename_suffix=filename_suffix,
        filename_extension=filename_extension,
        directory=directory
    )
    process.start()


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
