from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in background
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Set up Selenium WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Website to scrape
website_url = "https://shuvomistry.alchosting.xyz"
print(f"Fetching content from: {website_url}")
driver.get(website_url)

# Wait for JavaScript to load
time.sleep(5)

# Extract all links from homepage
soup = BeautifulSoup(driver.page_source, "html.parser")
links = set()

# Find all <a> tags and extract href values
for a_tag in soup.find_all("a", href=True):
    link = a_tag["href"]
    if link.startswith("/") or website_url in link:  # Ensure internal links only
        full_link = website_url + link if link.startswith("/") else link
        links.add(full_link)

print(f"Found {len(links)} pages to scrape.")

# Store scraped data
all_text_content = ""

# Loop through each page and extract content
for page_url in links:
    print(f"Scraping: {page_url}")
    driver.get(page_url)
    time.sleep(5)  # Wait for page to load

    page_soup = BeautifulSoup(driver.page_source, "html.parser")
    text_content = page_soup.get_text()
    
    all_text_content += f"\n\n=== {page_url} ===\n\n{text_content}"

# Save extracted text
with open("extracted_all_pages.txt", "w", encoding="utf-8") as file:
    file.write(all_text_content)

print("✅ Scraping completed! Check 'extracted_all_pages.txt' for results.")

# Close the browser
driver.quit()
