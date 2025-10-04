# Imports
from enum import Enum


class FileExtension(str, Enum):
    """Name/value pairs for filename extensions; works well with cli."""
    json = 'json'
    jsonl = 'jsonl'
    csv = 'csv'
    xml = 'xml'