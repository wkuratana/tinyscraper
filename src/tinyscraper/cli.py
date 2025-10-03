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
        help="Output filename, not including type extension."), 
        '--filename', 
        '-fn'
    ] = None,
    filename_suffix: Annotated[str|None, typer.Option(
        help="Suffix for ouput filename. Not the filename extension."), 
        '--filename_suffix', 
        '-fns'
    ] = None,
    filename_extension: Annotated[FileExtension, typer.Option(
        help="Output filename extension. E.g. 'json', 'csv'."), 
        '--filename_extension', 
        '-fne'
    ] = FileExtension.json,
    directory: Annotated[str|None, typer.Option(
        help="Directory where output files will be written."),
        '--directory',
        '-d'
    ] = None
    # TODO: Add arguments for Scrapy args/adjustments
):
    # TODO: Change once api file is updated
    scrape_thread_to_json(url, site_name=filename_suffix)
        

if __name__ == '__main__':
    app()