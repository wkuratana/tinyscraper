# Imports
from scrapy.item import Item, Field

class PostItem(Item):
    """Represents a single post in a thread."""
    author = Field()
    content = Field()
    image_url = Field(default=None)
    is_op = Field()
    linked_to_ids = Field()
    post_id = Field()
    timestamp = Field()

class ThreadItem(Item):
    """Represents an entire thread, of multiple posts."""
    board = Field()
    posts = Field()
    thread_id = Field()
    title = Field()