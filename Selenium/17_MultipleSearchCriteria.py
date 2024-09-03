from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.thebetterindia.com/topics/civil-service/")
driver.maximize_window()
time.sleep(10)

all_posts = {}
urls = []
categories = driver.find_elements(
    By.XPATH, "//div[@class='stickyfooterinner scrollX-box']//li/a"
)

for category in categories:
    urls.append(category.get_attribute("href"))
print(urls)
print()

for url in urls:
    titles = []
    print(f"\nScanning posts of {url}")
    driver.get(url)
    time.sleep(5)
    posts = driver.find_elements(
        By.XPATH, "//div[@class='d-flex flex-wrap justify-content-between']//h3/a"
    )
    for post in posts:
        titles.append(post.text)
    all_posts[url] = titles
    # print(all_posts)

print(all_posts)
