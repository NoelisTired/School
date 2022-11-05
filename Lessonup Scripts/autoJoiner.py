import os
import time
try:
    import webdriver_manager
    import selenium
except:
    os.system("pip install selenium webdriver-manager")

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def clear():
    os.system('cls')
    print("Lessonup autoJoiner.\nMade by Boy\n-------------------\n")


loggedIn = 0
nameList = []
clear()
lessonupCode = input("Lessonup code: ")
names = input("Number of account names seperated by ;\n")

options = webdriver.EdgeOptions()
options.add_argument("--log-level=3")
options.add_argument('--headless')

clear()
for accName in names.split(";"):
    nameList.append(accName)
print(f"Account names: {nameList}\n")

for name in nameList:
    driver = webdriver.Edge(
        EdgeChromiumDriverManager().install(), options=options)
    driver.get(f"https://lessonup.app/?lang=nl&code={lessonupCode}")
    WebDriverWait(driver, 30).until(
        EC.url_contains("https://lessonup.app/player/"))
    time.sleep(.7)
    driver.find_element(
        By.XPATH, "(//span[text()='English']/following::input)[1]").send_keys(f"{name}", Keys.RETURN)
    loggedIn += 1
    clear()
    print(
        f"Lessonup Code: {lessonupCode}\nAccount names: {nameList} - amount:{len(nameList)}\nAccounts logged in: {loggedIn}")

clear()
print(
    f"Lessonup Code: {lessonupCode}\nAccount names: {nameList} - amount:{len(nameList)}\nAccounts logged in: {loggedIn}")

options.remove_argument('--headless')
driver = webdriver.Edge(
    EdgeChromiumDriverManager().install(), options=options)
driver.get("https://www.rule34.xxx/index.php?page=post&s=list&tags=futanari")
