# Imports
import pytest
from scrapy.http import HtmlResponse
from scrapy.exceptions import UsageError
from tinyscraper.spiders.tinyboard import TinyboardSpider
from tinyscraper.types import FileExtension


def test_parse_custom_filename_on_homepage_raises_error():
    """
    Tests that using a custom filename on a non-thread page
    correctly raises a UsageError.
    """
    # Instantiate the spider directly with the arguments that cause the error
    spider = TinyboardSpider(
        filename='custom',
        filename_suffix='',
        filename_extension=FileExtension.json,
        directory='data'
    )

    # Create a mock Scrapy Response object to simulate a homepage
    # (This response does NOT contain a <div id="thread_...">)
    mock_homepage_url = 'https://example.com/board/index.html'
    mock_response = HtmlResponse(
        url=mock_homepage_url,
        body='<html><body><a href="/res/123.html">Thread</a></body></html>',
        encoding='utf-8'
    )

    # Call the parse method directly and assert that it raises the correct exception
    with pytest.raises(UsageError):
        list(spider.parse(mock_response))