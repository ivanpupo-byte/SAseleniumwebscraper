from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key, Controller
import time
from bs4 import BeautifulSoup
import bs4 as bs
from selenium.common.exceptions import NoSuchElementException


keyboard = Controller()

options = Options()
options.binary_location = r'C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe'
driver_path = r'C:\Users\ivan\Desktop\New folder\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(options=options, executable_path=driver_path)


driver.get("https://www.optionslam.com/earnings/stocks/CHWY")
driver.maximize_window()


time.sleep(.5)

k = 1

while k < 23:

    time.sleep(.5)

    row = str(k+3)

    stringeEPSxpath = """/ html / body / table[2] / tbody / tr / td[2] / table[2] / tbody / tr["""+row+"""] / td[1]"""
    elem1 = driver.find_element_by_xpath(stringeEPSxpath)
    Date = elem1.text

    file1 = open("myfile.txt", "a")
    L = [Date+"\n"]
    file1.writelines(L)
    file1.close()  # to change file access modes

    k = k + 1

    time.sleep(.5)

driver.close()