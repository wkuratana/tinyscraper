# Imports
from dataclasses import dataclass


@dataclass(frozen=True)
class Post:
    """Represents a single post in a thread."""
    author: str
    content: str
    post_id: str
    image_url: str
    replied_to_ids: set[str]
    timestamp: str


@dataclass(frozen=True)
class Thread:
    """Represents an entire thread, of multiple posts."""
    board: str
    thread_id: str
    posts: set[Post]
    title: str