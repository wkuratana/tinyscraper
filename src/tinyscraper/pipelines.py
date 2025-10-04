# Imports
import os
from scrapy.exporters import JsonItemExporter, JsonLinesItemExporter, CsvItemExporter, XmlItemExporter
from .spiders.tinyboard import TinyboardSpider


class PerItemFilePipeline:
    """Pipeline to write each thread to a file, with variable file types."""

    # Map extensions to Scrapy Exporter classes
    EXPORTER_MAPPING = {
        'json': JsonItemExporter,
        'jsonl': JsonLinesItemExporter,
        'csv': CsvItemExporter,
        'xml': XmlItemExporter,
    }
    # Map extensions to specific keyword arguments for each exporter
    EXPORTER_KWARGS = {
        'json': {'encoding': 'utf-8', 'indent': 4},
        'jsonl': {'encoding': 'utf-8'},
    }

    def open_spider(self, spider: TinyboardSpider):
        self.dir_path = os.path.join(
            spider.directory,
            spider.scrape_time.strftime('%Y%m%dT%H:%M:%S'),
        )
        os.makedirs(self.dir_path, exist_ok=True)

    def process_item(self, item, spider: TinyboardSpider):
        """Write out each ThreadItem into its own file."""
        # Each item should be a ThreadItem

        ext = spider.filename_extension.value
        exporter_class = self.EXPORTER_MAPPING.get(ext)

        if not exporter_class:
            raise Exception(
                "Error: Extension not supported"
            )

        if spider.filename is not None:
            filepath = os.path.join(
                self.dir_path,
                f"{spider.filename}.{ext}"
            )
        else:
            filepath = os.path.join(
                self.dir_path,
                f"thread_{item['thread_id'][0]}_"
                f"{spider.filename_suffix}.{ext}"
            )

        # Get specific kwargs for this exporter, or an empty dict if none are defined
        kwargs = self.EXPORTER_KWARGS.get(ext, {})
        
        with open(filepath, 'wb') as f:
            exporter = exporter_class(f, **kwargs)  # type: ignore
            exporter.start_exporting()
            exporter.export_item(item)
            exporter.finish_exporting()
        
        return item