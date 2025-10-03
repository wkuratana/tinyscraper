![Tinyscraper logo](/assets/Tinyscraper_logo.png)

# What is Tinyscraper?

Tinyscraper is a Python package that is designed to help with scraping post data from imageboards built using Tinyboard (and Tinyboard forks, such as vichan, etc.) for corpus analysis. Tinyscraper aims to be a helpful tool for both people familiar with building web scraping tools, and people who are not familiar/comfortable with working in Python.

## Feature Implementation Status
- [X] Basic Scrapy Spider functionality
- [ ] More functional API/CLI
- [ ] Thread post content formatting
- [ ] Publish package to PyPi

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

# Installation
Tinyscraper is still under development, and is not yet in a "usable" state. 

Tinyscraper does, however, still provide a good starting point for any Scrapy projects designed to scrape from Tinyboard sites. 

In order to install the package, please install it from the GitHub repository; in the future, the package will be published to PyPi and installable using `pip install tinyscraper`.

Be sure to use a virtual environment:
```bash
python3 -m venv venv
```
Then activate the virtual environment:
```bash
source venv/bin/activate
```
Finally, install the package:
```bash
pip install git+https://github.com/wkuratana/tinyscraper.git
```

# Usage
(This section will be updated once the API/CLI is implemented.)

For the time being, you can scrape a specific thread from a Tinyboard website, and its data will be exported to a JSON file in a local `data/` directory.

After installation, run:
```bash
tinyscraper
```
You will be prompted to enter a URL, then a site name. For the URL, be sure to pass a URL to a specific thread (for now). For the site name, anything you enter will be used in the JSON file name on export.

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

# License
This project is licensed under the [GPL-3.0 license](LICENSE).

