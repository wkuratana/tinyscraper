# Imports
from enum import Enum


class FileExtension(str, Enum):
    json = 'json'
    jsonl = 'jsonl'
    csv = 'csv'
    xml = 'xml'