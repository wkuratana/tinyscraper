<p align="center">
  <img alt="Tinyboard logo" src="assets/Tinyscraper_logo_new_blacktxt.svg#gh-light-mode-only"/>
  <img alt="Tinyboard logo" src="assets/Tinyscraper_logo_new_whitetxt.svg#gh-dark-mode-only"/>
</p>

![GitHub License](https://img.shields.io/github/license/wkuratana/tinyscraper) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tinyscraper) ![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/wkuratana/tinyscraper)

<h1 align="left">What is Tinyscraper?</h1>

Tinyscraper is a Python package that is designed to help with scraping post data from imageboards built using Tinyboard (and Tinyboard forks, such as vichan, etc.) for corpus analysis. Tinyscraper aims to be a helpful tool for both people familiar with building web scraping tools, and people who are not familiar/comfortable with working in Python.

<h2 align="left">Table of Contents</h2>  

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

<h1 align="left">Installation</h1>

In order to use the Tinyscraper package, please install it from PyPi.

> [!TIP]  
> It is a good idea to install Tinyscraper in a virtual environment!
> ```bash
> python3 -m venv venv
> ```
> ```bash
> source venv/bin/activate
> ```

To install the Tinyscraper package from PyPi:  
```bash
pip install tinyscraper
```
You can also install the Tinyscraper package from the GitHub repository:
```bash
pip install git+https://github.com/wkuratana/tinyscraper.git
```

<h1 align="left">Usage</h1>

> [!IMPORTANT]  
> Tinyscraper is designed to be polite and respectful.
> It does not currently—and will not in the future—facilitate any behavioral modifications that may overload a website or ignore explicit anti-scraping requests.

Tinyscraper's default behavior is as follows:

1. Visit the URL passed as an argument.
2. If the URL links to a specific thread, then scrape the thread. If the URL links to a homepage or a catalog page, then travel to each thread link on the page and scrape each thread.
3. Write out each scraped thread to its own JSON file in a local `data/` directory.

You can use optional arguments to change the output file type (JSON, JSONL, CSV, XML) and the output directory. You can also adjust the naming scheme of the output file. **You do not need to tell Tinyscraper if the URL links to a thread, homepage, or catalog page.** Tinyscraper can determine that itself.

Once installed, you can check to see the available arguments at any time using:
```bash
tinyscraper --help
```

<h2 align="left">Simple Scraping</h2>

The simplest command you can run is:
```bash
tinyscraper <url>
```
(Replace `<url>` with an actual URL).  

You can use any absolute URL that links to a homepage, to a catalog page, or to a specific thread (of a Tinyboard-based imageboard). 

<h2 align="left">Optional Arguments</h2>

Tinyscraper's default file naming convention is `thread_<thread_id>_tinyboard.json`.

To change the filename entirely, use `--filename` or `-fn`:
```bash
tinyscraper --filename <name> <url>
```

> [!NOTE]
> Do not add the filename extension to any filename you use.
> See how to change the file type below.

> [!WARNING]
> You can only use `--filename` or `-fn` if you pass a URL to a specific thread, **not a homepage or catalog page**.
> See how else you can modify filenames below.

To change the suffix used in the default file naming convention (which is `tinyboard` by default), use `--filename_suffix` or `-fns`:
```bash
tinyscraper --filename_suffix <suffix> <url>
```

To change the output file type, use `--filename_extension` or `-fne`:
```bash
tinyscraper --filename_extension <json|jsonl|csv|xml> <url>
```

To change the output directory, use `--directory` or `-d`:
```bash
tinyscraper --directory <path> <url>
```

<h3 align="left">Example</h3>

```bash
tinyscraper -fns testchan -fne jsonl -d test_data <url>
```

The command above visits the URL, then scrapes the thread data into a `test_data/` folder. The output file is named `thread_<thread_id>_testchan.jsonl`

<h2 align="left">API</h2>

Tinyscraper is designed to be used through both its CLI and its API. You can also install and use Tinyscraper as a dependency for other projects. Please reference the docstrings in `api.py` if you would like to use Tinyscraper without its CLI.

Tinyscraper is built leveraging Scrapy. It can be easily modified if you find that it would better suit your use case with different functionality.

<h1 align="left">Contributing</h1>

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

<h1 align="left">License</h1>

This project is licensed under the [GPL-3.0 license](LICENSE).

