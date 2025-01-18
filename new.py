import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Load environment variables from .env file
load_dotenv()
USERNAME = os.getenv("LEETCODE_USERNAME")
PASSWORD = os.getenv("LEETCODE_PASSWORD")

# Function to log in to LeetCode
def login_to_leetcode(driver):
    driver.get("https://leetcode.com/accounts/login/")
    
    # Wait for login page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "login"))
    )
    
    # Enter login credentials
    driver.find_element(By.NAME, "login").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    
    # Wait for the dashboard to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "nav-item-container"))
    )

# Function to scrape submissions
def scrape_submissions(driver):
    driver.get("https://leetcode.com/submissions/")
    
    submissions = []
    while True:
        # Wait for submissions to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "status-cell"))
        )
        
        rows = driver.find_elements(By.CSS_SELECTOR, ".ant-table-row")
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            submission = {
                "Problem": cells[1].text,
                "Status": cells[2].text,
                "Language": cells[3].text,
                "Time": cells[4].text
            }
            submissions.append(submission)
        
        # Try to go to the next page
        next_button = driver.find_element(By.CLASS_NAME, "ant-pagination-next")
        if "ant-pagination-disabled" in next_button.get_attribute("class"):
            break
        next_button.click()
        time.sleep(2)
    
    return submissions

# Main function
def main():
    if not USERNAME or not PASSWORD:
        print("Please set your LeetCode username and password in the .env file.")
        return
    
    # Set up the Selenium WebDriver
    driver = webdriver.Chrome()  # Replace with the path to your WebDriver if necessary
    driver.maximize_window()
    
    try:
        # Log in and scrape submissions
        login_to_leetcode(driver)
        submissions = scrape_submissions(driver)
        
        # Save submissions to a CSV file
        df = pd.DataFrame(submissions)
        df.to_csv("leetcode_submissions.csv", index=False)
        print("Submissions saved to leetcode_submissions.csv")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
