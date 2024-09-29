# HTML Scraper

This project is a simple HTML scraper that extracts the inner content of a webpage, excluding headers, footers, and other unwanted sections.

## Features

- Scrapes the main content of a specified webpage
- Removes unwanted elements like headers and footers
- Saves the extracted HTML content to a file
- Implements error handling and logging

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+
- pip (Python package installer)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/html-scraper.git
   cd html-scraper
   ```

2. Create a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
      deactivate
   ```

3. Install the required packages:
   ```
   pip install  beautifulsoup4
   pip install requests
   ```
   or 
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Open `html_scrapper.py` and modify the URL and output file name in the `scrape_inner_html()` function call at the bottom of the file.

2. Run the script:
   ```
   python html_scrapper.py
   ```

3. Check the output file (e.g., `output.html`) for the scraped content.

## Customization

- Adjust the `main_content = soup.find('div', class_='content')` line in `html_scrapper.py` to match the structure of the website you're scraping.
- Modify the `for unwanted in main_content.find_all(['header', 'footer'])` line to remove additional unwanted elements.

## Contributing

Contributions to this project are welcome. Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for educational purposes only. Always respect the website's robots.txt file and terms of service when scraping content.



(.venv) 0:02:37~/Software/Scrapper/HTML_scraper√  (master|…)    deactivate
0:02:52~/Software/Scrapper/HTML_scraper√  (master|✚1…)    rm -rf .venv
0:02:57~/Software/Scrapper/HTML_scraper√  (master|✚1…)    python3 -m venv .venv
0:03:12~/Software/Scrapper/HTML_scraper√  (master|✚1…)    source .venv/bin/activate
(.venv) 0:03:14~/Software/Scrapper/HTML_scraper√  (master|✚1…)    python -m pip install --upgrade pip
Requirement already satisfied: pip in ./.venv/lib/python3.12/site-packages (24.0)
Collecting pip
  Using cached pip-24.2-py3-none-any.whl.metadata (3.6 kB)
Using cached pip-24.2-py3-none-any.whl (1.8 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 24.0
    Uninstalling pip-24.0:
      Successfully uninstalled pip-24.0
Successfully installed pip-24.2
(.venv) 0:03:28~/Software/Scrapper/HTML_scraper√  (master|✚1…)    python -m pip install requests beautifulsoup4
Collecting requests
  Using cached requests-2.32.3-py3-none-any.whl.metadata (4.6 kB)
Collecting beautifulsoup4
  Using cached beautifulsoup4-4.12.3-py3-none-any.whl.metadata (3.8 kB)
Collecting charset-normalizer<4,>=2 (from requests)
  Using cached charset_normalizer-3.3.2-cp312-cp312-macosx_10_9_x86_64.whl.metadata (33 kB)
Collecting idna<4,>=2.5 (from requests)
  Using cached idna-3.10-py3-none-any.whl.metadata (10 kB)
Collecting urllib3<3,>=1.21.1 (from requests)
  Using cached urllib3-2.2.3-py3-none-any.whl.metadata (6.5 kB)
Collecting certifi>=2017.4.17 (from requests)
  Using cached certifi-2024.8.30-py3-none-any.whl.metadata (2.2 kB)
Collecting soupsieve>1.2 (from beautifulsoup4)
  Using cached soupsieve-2.6-py3-none-any.whl.metadata (4.6 kB)
Using cached requests-2.32.3-py3-none-any.whl (64 kB)
Using cached beautifulsoup4-4.12.3-py3-none-any.whl (147 kB)
Using cached certifi-2024.8.30-py3-none-any.whl (167 kB)
Using cached charset_normalizer-3.3.2-cp312-cp312-macosx_10_9_x86_64.whl (122 kB)
Using cached idna-3.10-py3-none-any.whl (70 kB)
Using cached soupsieve-2.6-py3-none-any.whl (36 kB)
Using cached urllib3-2.2.3-py3-none-any.whl (126 kB)
Installing collected packages: urllib3, soupsieve, idna, charset-normalizer, certifi, requests, beautifulsoup4
Successfully installed beautifulsoup4-4.12.3 certifi-2024.8.30 charset-normalizer-3.3.2 idna-3.10 requests-2.32.3 soupsieve-2.6 urllib3-2.2.3
(.venv) 0:03:39~/Software/Scrapper/HTML_scraper√  (master|✚1…) pip install requests
Requirement already satisfied: requests in ./.venv/lib/python3.12/site-packages (2.32.3)
Requirement already satisfied: charset-normalizer<4,>=2 in ./.venv/lib/python3.12/site-packages (from requests) (3.3.2)
Requirement already satisfied: idna<4,>=2.5 in ./.venv/lib/python3.12/site-packages (from requests) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in ./.venv/lib/python3.12/site-packages (from requests) (2.2.3)
Requirement already satisfied: certifi>=2017.4.17 in ./.venv/lib/python3.12/site-packages (from requests) (2024.8.30)
(.venv) 0:04:07~/Software/Scrapper/HTML_scraper√  (master|✚1…)    python -m pip install requests beautifulsoup4
Requirement already satisfied: requests in ./.venv/lib/python3.12/site-packages (2.32.3)
Requirement already satisfied: beautifulsoup4 in ./.venv/lib/python3.12/site-packages (4.12.3)
Requirement already satisfied: charset-normalizer<4,>=2 in ./.venv/lib/python3.12/site-packages (from requests) (3.3.2)
Requirement already satisfied: idna<4,>=2.5 in ./.venv/lib/python3.12/site-packages (from requests) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in ./.venv/lib/python3.12/site-packages (from requests) (2.2.3)
Requirement already satisfied: certifi>=2017.4.17 in ./.venv/lib/python3.12/site-packages (from requests) (2024.8.30)
Requirement already satisfied: soupsieve>1.2 in ./.venv/lib/python3.12/site-packages (from beautifulsoup4) (2.6)
(.venv) 0:04:24~/Software/Scrapper/HTML_scraper√  (master|✚1…)    pip list
Package            Version
------------------ ---------
beautifulsoup4     4.12.3
certifi            2024.8.30
charset-normalizer 3.3.2
idna               3.10
pip                24.2
requests           2.32.3
soupsieve          2.6
urllib3            2.2.3
(.venv) 0:04:31~/Software/Scrapper/HTML_scraper√  (master|✚1…) 