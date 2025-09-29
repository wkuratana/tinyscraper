![Tinyscraper logo](/assets/Tinyscraper_logo.png)

# What is Tinyscraper?

Tinyscraper is a Python package that is designed to help with scraping post data from imageboards built using Tinyboard (and Tinyboard forks, such as vichan, etc.) for corpus analysis. Tinyscraper aims to be a helpful tool for both people familiar with building web scraping tools, and people who are not familiar/comfortable with working in Python.

## Feature Implementation Status
- [X] Basic Scrapy Spider functionality
- [ ] Thread post content formatting
- [ ] API/CLI
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
```bash
pip install git+https://github.com/wkuratana/tinyscraper.git
```

# Usage
(This section will be updated once the API/CLI is implemented.)

For the time being, Tinyscraper includes a Scrapy Spider which can be used to crawl and scrape data from any imageboard homepage, catalog page, or specific thread URL.

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

# License
This project is licensed under the [GPL-3.0 license](LICENSE).

