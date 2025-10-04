# Imports
import datetime
import logging
import scrapy
from scrapy.loader import ItemLoader
from ..types import FileExtension
from ..items import PostItem, ThreadItem


class TinyboardSpider(scrapy.Spider):
    """
    Scrapes threads and posts from Tinyboard-based sites.
    Can be started on an homepage, catalog page, or a specific thread URL.
    """
    name = 'tinyboard'

    def __init__(
        self, 
        filename: str|None,
        filename_suffix: str,
        filename_extension: FileExtension, 
        directory: str, 
        *args, 
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.scrape_time = datetime.datetime.now()
        self.filename = filename
        self.filename_suffix = filename_suffix
        self.filename_extension = filename_extension
        self.directory = directory

    def parse(self, response):
        """
        Routes the response to the correct parser.
        Checks if we're on a thread page or a homepage/catalog page.
        """
        # A thread page contains a single div with an ID like "thread_12345"
        is_thread_page = response.css('div[id^="thread_"]')
        if is_thread_page:
            yield from self._parse_thread_page(response)
        else:
            if self.filename is None:
                try:
                    # On an homepage/catalog, find all thread links 
                    # and crawl them
                    thread_links = response.css(
                        'a[href*="/res/"]::attr(href)'
                    ).getall()
                    yield from response.follow_all(
                        thread_links, callback=self._parse_thread_page
                    )
                except Exception as e:
                    logging.error(
                        "Error when scraping expected homepage"
                        f" or catalog: {e}"
                    )
            else:
                # You cannot have a custom filename for every file
                raise Exception(
                    "Error: You cannot use a custom filename "
                    "with a catalog or homepage."
                )

    def _parse_thread_page(self, response):
        """Parses all posts within a single thread page."""
        thread_loader = ItemLoader(item=ThreadItem(), response=response)
        # Scrape thread-level info
        thread_loader.add_css(
            'thread_id', 
            'div[id^="thread_"]::attr(id)', re=r'(\d+)'
        )
        thread_loader.add_css(
            'board', 
            'header h1::text', re=r'/(.*?)/'
        )
        thread_loader.add_css(
            'title', 
            'title::text', re=r' - (.*)'
        )
        # Then, parse each post
        all_posts = []
        for post_el in response.css('div.post'):
            all_posts.append(self._parse_post(post_el, response))
        
        thread_loader.add_value('posts', all_posts)
        yield thread_loader.load_item()

    def _parse_post(self, post_selector, response):
        """Parses a single post element from a thread."""
        post_loader = ItemLoader(item=PostItem(), selector=post_selector)
        # Check if this post is the OP
        is_op = 'op' in post_selector.attrib.get('class', '')
        post_loader.add_value(
            'is_op', 
            is_op
        )
        # Scrape standard post fields
        post_loader.add_css(
            'post_id', 
            'a.post_no::text', 
            re=r'(\d+)'
        )
        post_loader.add_css(
            'author', 
            'span.name::text'
        )
        post_loader.add_css(
            'timestamp', 
            'time::attr(datetime)'
        )
        post_loader.add_css(
            'content', 
            'div.body'
        )
        post_loader.add_css(
            'linked_to_ids', 
            'div.body a::text', 
            re=r'>>(?:>)?/?(.+)'
        )
        # Look for any image link inside the post div first
        image_css = (
            'div.files a::attr(href), ' 
            'p.fileinfo a::attr(href)'
        )
        relative_url = post_selector.css(image_css).get()
        # Handle edge case where the OP's image info is a sibling element
        if not relative_url and is_op:
            # Find the first preceding sibling of current element that is 
            # either a div.files or a p.fileinfo, then get href from its link
            xpath_query = (
                './preceding-sibling::*['
                'self::div[@class="files"] or '
                'self::p[@class="fileinfo"]'
                '][1]/a/@href'
            )
            relative_url = post_selector.xpath(xpath_query).get()
        if relative_url:  
            full_url = response.urljoin(relative_url)
            post_loader.add_value(
                'image_url',  # If not, default is None
                full_url
            )
        
        return post_loader.load_item()
