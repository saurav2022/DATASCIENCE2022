from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://www.myneta.info/LokSabha2024/")
driver.maximize_window()

states = driver.find_elements(
    By.XPATH,
    "//div[@class='w3-dropdown-click w3-block']/button[@class='w3-button w3-block dropbtnJS']",
)

# Extracting all the states and their ids
state_map = {}
for state in states:
    id = state.get_attribute("onclick").split(",")[1].split("'")[1]
    name = state.text
    state_map[name] = id

# Extracting state wise politicians' details
contestants_list = []
for state in state_map.items():
    state_name, state_id = state
    print(f"{state_id} --> {state_name}")
    # if state_name not in ("ANDAMAN AND NICOBAR ISLANDS"): #     continue
    print(f"Scanning all contestant details of {state_name}....")
    for page_id in range(1, 15):
        print(f"\t Scanning page number {page_id}")
        driver.get(
            f"https://www.myneta.info/LokSabha2024/index.php?action=show_constituencies&state_id={state_id}&page={page_id}"
        )
        time.sleep(1)

        contestants = driver.find_elements(
            By.XPATH, "//table[@class='w3-table w3-bordered']//tr"
        )
        if len(contestants) == 0:
            print(f"\t No more canidates for this state.\n")
            break
        for i in range(2, len(contestants) + 1):
            dtls = []
            state_can_id = driver.find_element(
                By.XPATH, f"//table[@class='w3-table w3-bordered']//tr[{i}]/td[1]"
            ).text
            name = driver.find_element(
                By.XPATH, f"//table[@class='w3-table w3-bordered']//tr[{i}]/td[2]"
            ).text
            party = driver.find_element(
                By.XPATH, f"//table[@class='w3-table w3-bordered']//tr[{i}]/td[3]"
            ).text
            cc = driver.find_element(
                By.XPATH, f"//table[@class='w3-table w3-bordered']//tr[{i}]/td[4]"
            ).text
            edu = driver.find_element(
                By.XPATH, f"//table[@class='w3-table w3-bordered']//tr[{i}]/td[5]"
            ).text
            age = driver.find_element(
                By.XPATH, f"//table[@class='w3-table w3-bordered']//tr[{i}]/td[6]"
            ).text
            assets = driver.find_element(
                By.XPATH, f"//table[@class='w3-table w3-bordered']//tr[{i}]/td[7]"
            ).text

            assets = (
                assets.split("~")[0]
                .replace(",", "")
                .replace("Rs ", "")
                .replace("\r", "")
                .replace("\n", "")
            )

            dtls.append(state_name)
            dtls.append(state_can_id)
            dtls.append(name)
            dtls.append(party)
            dtls.append(cc)
            dtls.append(edu)
            dtls.append(age)
            dtls.append(assets)
            contestants_list.append(dtls)

# print(contestants_list)

import pandas as pd

df = pd.DataFrame(
    contestants_list,
    columns=["State", "State_Can_ID", "Name", "Party", "CC", "Edu", "Age", "Assets"],
)
df.to_csv("contestants.csv", encoding="utf-8", index=False)

print("Done!")

driver.quit()
