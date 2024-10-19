# Web-Crawling
Web Crawling Task - BAB International 

# Web Crawling Script README

## Project Overview
This Python script scrapes data from a website (https://muqawil.org/) containing contractor information and saves it to an Excel file. It utilizes the `requests`, `BeautifulSoup`, and `pandas` libraries for web scraping and data processing.

## Dependencies
- Python 3.x
- requests
- BeautifulSoup (bs4)
- pandas

## How to Run
1. Clone the repository or download the Python script.
2. Install the required dependencies using pip:
   ```bash
   pip install requests beautifulsoup4 pandas

3. Run the script in a Python environment:
   python your_script_name.py
4. Follow the prompts to enter the number of pages to scrape and the file path to save the data.

# Code Structure
Input Processing: Takes user input for the number of pages and the Excel file path.
Data Scraping: Scrapes company information from each page of the website using requests and BeautifulSoup.
Data Processing: Extracts relevant details such as company name, membership number, phone, email, city, and activities.
Data Saving: Saves the extracted data to an Excel file at the specified file path.

# Functions
main(excel_file_path, positive): Main function that orchestrates the data scraping, processing, and saving.
get_company_info(companies): Helper function to extract information for each company from the website.

# Sample Run
Enter the number of pages to scrape: 10
Enter the file path to save the Excel file: /Users/Desktop/contractor_data.xlsx
The script will start processing and display progress updates for each page scraped.

# Note
This script is tailored to scrape contractor information from the muqawil.org website. Modify the URL and HTML parsing as needed for different websites.
