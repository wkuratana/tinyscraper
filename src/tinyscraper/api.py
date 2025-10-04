# Imports
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
    Scrape a homepage, catalog page, or a specific thread URL to ind. files.

    If a specific thread URL is passed, then a single file will be written 
    out. If a homepage or catalog page is passed, then a file for each listed
    thread (formatted as though each thread was passed individually) will
    be written out.

    Args:
        url (str): Absolute URL to a homepage, catalog, or thread.
        filename (str|None): Name of file written out.
        filename_suffix (str): End of default file numbering scheme. See docs.
        filename_extension (FileExtension): File type.
        directory (str): Directory where all files will go after scraping.
    """
    process = CrawlerProcess(settings={
        'LOG_LEVEL': 'WARNING',
        'ROBOTSTXT_OBEY': True,  # Be ethical.
        'AUTOTHROTTLE_ENABLED': True,  # Don't screw with their server load.
        'CONCURRENT_REQUESTS': 16,
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
