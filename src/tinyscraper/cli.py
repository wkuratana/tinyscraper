# Imports
import typer
from typing_extensions import Annotated
from .api import scrape_from_url
from .types import FileExtension


app = typer.Typer()

@app.command()
def scrape(
    url: Annotated[str, typer.Argument(
        help="Homepage, catalog, or thread URL."
    )], 
    filename: Annotated[str|None, typer.Option(
        '--filename', 
        '-fn',
        help="Output filename, not including type extension.")
    ] = None,
    filename_suffix: Annotated[str, typer.Option(
        '--filename_suffix', 
        '-fns',
        help="Suffix for ouput filename. Not the filename extension.")
    ] = 'tinyboard',
    filename_extension: Annotated[FileExtension, typer.Option(
        '--filename_extension', 
        '-fne',
        help="Output filename extension. E.g. 'json', 'csv'.")
    ] = FileExtension.json,
    directory: Annotated[str, typer.Option(
        '--directory',
        '-d',
        help="Where output files will be written. Default is local data/.")
    ] = 'data'
    # TODO: Add arguments for Scrapy args/adjustments
):
    scrape_from_url(
        url, 
        filename, 
        filename_suffix, 
        filename_extension, 
        directory
    )
        

if __name__ == '__main__':
    app()