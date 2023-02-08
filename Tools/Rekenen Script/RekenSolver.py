# Made By:
# Boy & Noël
try:
    import os
    import time
    import selenium
    import win32api
except:
    os.system("pip install selenium pywin32 webdriver-manager colorama")

import os
import time
import selenium
import win32api
import threading
import json
import logging
import math
from selenium import webdriver
from colorama import Fore, init
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
init()


class Attributes:
    authors = "Sadcat & NoelP"
    version = "1.0.0"
    user = "Not yet Logged in"

    with open("config.json", "r") as f:
        config = json.load(f)
    email = config["Email"]
    password = config["Password"]

    def cmdTitle(self):
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(
            "RekenenSolver {} by Sadcat & NoelP > Last answer: NONE".format(self.version))

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.banner(self)

    def banner(self):
        print(Fore.LIGHTCYAN_EX,"RekenSolver by Sadcat & NoelP")
        print(Fore.LIGHTCYAN_EX,f"Account: {self.user}\n{'_' * 100}")

    def getDriver(self):
        self.clear(self)
        from webdriver_manager.chrome import ChromeDriverManager
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        driverChoice = input("Chrome / Edge: ")
        if driverChoice.lower() == "chrome":
            print("Webdriver: Chrome")
            options = webdriver.ChromeOptions()
            options.add_argument("--log-level=3")
            driver = webdriver.Chrome(
                ChromeDriverManager().install(), chrome_options=options)
        elif driverChoice.lower() == "edge":
            print("Webdriver: Edge")
            options = webdriver.EdgeOptions()
            options.add_argument("--log-level=3")
            driver = webdriver.Edge(
                EdgeChromiumDriverManager().install(), options=options)
        else:
            return False
        Attributes.start(self, driver)

    def start(self, driver):
        self.clear(self)
        driver.get("https://dashboard.uitgeverij-deviant.nl/")
        print(Fore.LIGHTCYAN_EX,f"Attempting to Login thru [https://dashboard.uitgeverij-deviant.nl/]")
        time.sleep(.75)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/section/form[1]"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/main/div/section[2]/form[1]/input[3]"))).send_keys("curio")
        time.sleep(.75)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/main/div/section[2]/ul[2]/li/div"))).click()
        #! END ASDF LOGIN
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div/div/form/div[2]/div[1]/input"))).send_keys(self.email)
        time.sleep(.75)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div/div/form/div[2]/div[2]/input"))).send_keys(self.password, Keys.RETURN)
        WebDriverWait(driver, 360).until(EC.url_contains(
            "https://dashboard.uitgeverij-deviant.nl/"))
        userdiv = WebDriverWait(driver, 360).until(EC.presence_of_element_located((By.XPATH, "/html/body/db-root/db-shell/udwc-sidenav-container/udwc-sidenav-content/div/header/db-shell-header/udwc-toolbar/udwc-profile-dropdown")))
        self.user = userdiv.get_attribute('caption')
        print(Fore.LIGHTCYAN_EX,f"Successfully logged in as: {self.user}")
        driver.get(
            "https://studiemeter.uitgeverij-deviant.nl/main/?screen=exercises&methodId=162&studyYearId=353&componentId=2775")
        self.getOpdracht(self, driver)

    def getOpdracht(self, driver):
        self.clear(self)
        print(Fore.LIGHTCYAN_EX,f"Click [F10] to solve the current sum")
        while win32api.GetKeyState(0xBE) < 0:
            time.sleep(1)

        self.idler(self, driver)

    def idler(self, driver):
        while True:
            if win32api.GetKeyState(0x79) < 0:  # ! . Indedrukt
                time.sleep(.75)
                threading.Thread(target=self.getSom, args=[
                                 self, driver]).start()
                time.sleep(.75)

    def getSom(self, driver):
        try:
            temp = driver.find_element(By.CSS_SELECTOR, "[id^='question_']")
            #! Bypass voor de anti bot check, letterlijk ander alfabet :kekw:
            som = temp.text.replace(",", ".").replace('=', '').replace(
                '×', '*').replace(':', '/').replace('−', "-")
            self.getAnswer(self, driver, som)
        except NoSuchElementException:
            print("Geen som gevonden.")
        except Exception as E:
            print("No support for Image/Text based sums.")

    def getAnswer(self, driver, som):
        if "√" in som:
            som = str(eval(f"math.sqrt({int(som)})")).replace(".", ",")
        answer = str(eval(som)).replace(".", ",")
        if answer.startswith("invalid syntax"):
            print("We're not able to solve questions that involve text")
        print(f"""
        ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
            | SUM: {som}          
            | ANSWER: {answer}                                      
        ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈ """)
        self.answerSubmission(self, driver, answer)

    def answerSubmission(self, driver, answer):
        import ctypes
        driver.find_element(
            By.XPATH, "/html/body/div[6]/div/exercise-container/div/div/div/exercise-item/div/div[2]/div/div/question-list/div/div/question-type2/div/html-block/type2-input/span/span/exercise-input/div/input").send_keys(answer, Keys.RETURN)
        ctypes.windll.kernel32.SetConsoleTitleW(
            "RekenenSolver by Sadcat & NoelP > Last answer: " + answer)


if __name__ == "__main__":
    logging.getLogger("webdriver-manager").setLevel(logging.WARNING)
    Attributes.cmdTitle(Attributes)
    while True:
        try:
            Attributes.getDriver(Attributes)
        except Exception as E:
            print(E)
            time.sleep(5)
            print("Please select another option")
