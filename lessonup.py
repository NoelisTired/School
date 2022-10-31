import sys, time, subprocess, requests, socket, random, os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.get("https://lessonup.app/?lang=nl&code=631689")
time.sleep(5)
print("sending")
driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div[1]/form/input[1]").send_keys("jamal", Keys.RETURN)
driver.quit()