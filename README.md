<p align="center">
  <img alt="Tinyboard logo" src="assets/Tinyscraper_logo_new_blacktxt.svg#gh-light-mode-only"/>
  <img alt="Tinyboard logo" src="assets/Tinyscraper_logo_new_whitetxt.svg#gh-dark-mode-only"/>
</p>

![GitHub License](https://img.shields.io/github/license/wkuratana/tinyscraper) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tinyscraper) ![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/wkuratana/tinyscraper)

<h1 align="left">What is Tinyscraper?</h1>

Tinyscraper is a Python package that is designed to help with scraping post data from imageboards built using Tinyboard (and Tinyboard forks, such as vichan, etc.) for corpus analysis. Tinyscraper aims to be a helpful tool for both people familiar with building web scraping tools, and people who are not familiar/comfortable with working in Python.

<h2 align="left">Feature Implementation Status</h2>  

- [X] Basic Scrapy Spider functionality  
- [ ] More functional API/CLI
- [ ] Thread post content formatting
- [ ] Publish package to PyPi

<h2 align="left">Table of Contents</h2>  

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

<h1 align="left">Installation</h1>

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

<h1 align="left">Usage</h1>

> [!IMPORTANT]  
> This section will be updated once the API/CLI is fully implemented.
> These instructions are not currently accurate, but there will be more helpful info when you run the command below.

For the time being, you can scrape a specific thread from a Tinyboard website, and its data will be exported to a JSON file in a local `data/` directory.

After installation, run:
```bash
tinyscraper
```

<h1 align="left">Contributing</h1>

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

<h1 align="left">License</h1>

This project is licensed under the [GPL-3.0 license](LICENSE).

