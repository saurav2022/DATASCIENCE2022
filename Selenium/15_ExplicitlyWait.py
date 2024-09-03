from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotVisibleException,
    ElementNotSelectableException,
)
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

# Explicit Wait
mywait = WebDriverWait(
    driver,
    10,
    poll_frequency=2,  # Poll every 2 seconds, if not available
    ignored_exceptions=[
        NoSuchElementException,
        ElementNotSelectableException,
        ElementNotVisibleException,
        Exception,
    ],
)

driver.get("https://www.google.com")
try:
    searchLink = mywait.until(EC.presence_of_element_located((By.NAME, "q")))
    searchLink.send_keys("Selenium")
    searchLink.submit()
except Exception as e:
    print(e)
finally:
    pass
    # driver.quit()
