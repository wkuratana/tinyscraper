# Imports
import typer
from typing_extensions import Annotated
from .api import FileExtension, scrape_thread_to_json


app = typer.Typer()

@app.command()
def scrape(
    url: Annotated[str, typer.Argument(
        help="Homepage, catalog, or thread URL."
    )], 
    filename: Annotated[str|None, typer.Option(
        '--filename', 
        '-n',
        help="Output filename, not including type extension.")
    ] = None,
    filename_suffix: Annotated[str|None, typer.Option(
        '--filename_suffix', 
        '-s',
        help="Suffix for ouput filename. Not the filename extension.")
    ] = 'tinyboard',
    filename_extension: Annotated[FileExtension, typer.Option(
        '--filename_extension', 
        '-e',
        help="Output filename extension. E.g. 'json', 'csv'.")
    ] = FileExtension.json,
    directory: Annotated[str, typer.Option(
        '--directory',
        '-d',
        help="Where output files will be written. Default is local data/.")
    ] = "data"
    # TODO: Add arguments for Scrapy args/adjustments
):
    # TODO: Change once api file is updated

    scrape_thread_to_json(url, site_name=filename_suffix)
        

if __name__ == '__main__':
    app()