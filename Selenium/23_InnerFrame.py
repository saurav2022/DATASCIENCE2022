from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://demo.automationtesting.in/Frames.html")

driver.find_element(
    By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']"
).click()

outerFrame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerFrame)

innerFrame = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(innerFrame)

driver.find_element(By.XPATH, "/html/body/section/div/div/div/input").send_keys(
    "House within a house"
)


driver.switch_to.parent_frame()
outerText = driver.find_element(By.XPATH, "/html/body/section/div/div/h5").text
print(outerText)
