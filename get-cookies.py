from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json

# Initialize WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run browser in headless mode
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Open a website
driver.get('https://www.facebook.com')

# Get cookies from the browser
cookies = driver.get_cookies()

# Custom format for cookies
custom_cookies = {}
desired_cookies = ['c_user', 'xs', 'datr', 'fr']
for cookie in cookies:
    name = cookie.get('name')
    value = cookie.get('value')
    if name in desired_cookies:
        custom_cookies[name] = value

# Print cookies in custom format
print(custom_cookies)

# Save cookies to a file in custom format
with open('custom_cookies.json', 'w') as file:
    json.dump(custom_cookies, file)

# Close the browser
driver.quit()