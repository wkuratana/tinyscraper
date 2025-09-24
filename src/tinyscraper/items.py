# Imports
import scrapy

class PostItem(scrapy.Item):
    """Represents a single post in a thread."""
    author = scrapy.Field()
    content = scrapy.Field()
    image_url = scrapy.Field()
    is_op = scrapy.Field()
    linked_to_ids = scrapy.Field()
    post_id = scrapy.Field()
    timestamp = scrapy.Field()

class ThreadItem(scrapy.Item):
    """Represents an entire thread, of multiple posts."""
    board = scrapy.Field()
    posts = scrapy.Field()
    thread_id = scrapy.Field()
    title = scrapy.Field()