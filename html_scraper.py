import requests
from bs4 import BeautifulSoup
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def scrape_inner_html(url, output_file):
    try:
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the main content (assuming it's inside a div with a class like 'content' or 'main')
        main_content = soup.find('div', class_='content')  # Adjust this based on the website structure
        if not main_content:
            logger.warning(f"Main content not found for {url}")
            return

        # Optionally, remove header and footer if they exist inside the main content
        for unwanted in main_content.find_all(['header', 'footer']):
            unwanted.extract()

        # Convert the main content back to a string (inner HTML)
        inner_html = str(main_content)

        # Save the HTML content to a file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(inner_html)

        logger.info(f"Inner HTML saved to {output_file}")

    except requests.RequestException as e:
        logger.error(f"Error fetching {url}: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

# Usage
scrape_inner_html('https://example.com/page', 'output.html')