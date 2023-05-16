from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import datetime

# Read the list of values from the text file
with open('file.txt', 'r') as f:
    values = [line.strip() for line in f]

# Initialize the WebDriver
driver = webdriver.Chrome('/path/to/chromedriver')

# Create a list to store skipped values
skipped_values = []

# Iterate over the values
for value in values:
    # Go to the webpage
    driver.get('http://www.example.com')

    # Find the search box, input the value, and press Enter
    search_box = driver.find_element(By.NAME, 'search_box')
    search_box.send_keys(value)
    search_box.send_keys(Keys.RETURN)  # press Enter

    try:
        # Wait for the page to load after submitting the search
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'element_on_page'))  # replace with an actual element on the page
        )

        # Find two values on the page
        value1 = driver.find_element(By.ID, 'value1_element').get_attribute('value')  # replace with the actual id
        value2 = driver.find_element(By.ID, 'value2_element').get_attribute('value')  # replace with the actual id

        # Check if value2 is today's date, if so skip to the next value
        if value2 == datetime.now().strftime('%Y-%m-%d'):  # adjust the date format as necessary
            print(f"Skipping value: {value}")
            skipped_values.append(value)
            continue

        # Input these values into another form on the same page
        form_field1 = driver.find_element(By.ID, 'form_field1')  # replace with the actual id
        form_field1.clear()
        form_field1.send_keys(value1)
        
        form_field2 = driver.find_element(By.ID, 'form_field2')  # replace with the actual id
        form_field2.clear()
        form_field2.send_keys(value2)

        # Submit the form
        submit_button = driver.find_element(By.ID, 'submit_button')  # replace with the actual id
        submit_button.click()

        # Wait for the page to load after submitting the form
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'element_on_page'))  # replace with an actual element on the page
        )

    except Exception as e:
        print(f"Error occurred: {e}")
        continue

# Close the browser
driver.quit()

# Write skipped values to a log file
with open('skipped.log', 'w') as f:
    for value in skipped_values:
        f.write(f"{value}\n")

print(f"Number of values skipped: {len(skipped_values)}")
