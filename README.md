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
   ```

3. Install the required packages:
   ```
   pip install  beautifulsoup4
   pip install requests
   or 
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