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


driver.get("https://seekingalpha.com/symbol/CHWY/earnings")
driver.maximize_window()



i = 1

while i < 20:
    row = str(i)

    EPS = driver.find_element_by_xpath("""/html/body/div[3]/div[1]/div/div/div/div/div[2]/div/section[6]/div[2]/div["""+row+"""]/div[1]/div/a/span[2]""")

    EPSTEXT = EPS.text

    EPSSPLIT = EPSTEXT.split("e")

    EPSNUMBER = EPSSPLIT[0]
    EPSBEAT = EPSSPLIT[1]

    EPSNUMBER = EPSNUMBER.replace("EPS", '')
    EPSNUMBER = EPSNUMBER.replace("of", '')
    EPSNUMBER = EPSNUMBER.replace("$", '')
    EPSNUMBER = EPSNUMBER.replace("b", '')
    EPSNUMBER = EPSNUMBER.replace("miss", '')
    EPSNUMBER = EPSNUMBER.replace(" ", '')

    #print(EPSNUMBER)

    EPSBEAT = EPSBEAT.replace("by", '')
    EPSBEAT = EPSBEAT.replace("at", '')
    EPSBEAT = EPSBEAT.replace("d", '')
    EPSBEAT = EPSBEAT.replace("$", '')
    EPSBEAT = EPSBEAT.replace(" ", '')

    #print(EPSBEAT)

    EPSNUMBERFLOAT = float(EPSNUMBER)
    EPSBEATFLOAT = float(EPSBEAT)

    ESTIMATEEPS = EPSNUMBERFLOAT - EPSBEATFLOAT

    ESTIMATEEPS = str(ESTIMATEEPS)

    #print(ESTIMATEEPS)

 #   / html / body / div[1] / div / main / div[3] / div[1] / div / form / div[2] / div[3] / input

    driver.get("https://www.calculatorsoup.com/calculators/algebra/percent-change-calculator.php")
    time.sleep(1)
    driver.find_element_by_xpath("""/html/body/div[1]/div/main/div[3]/div[1]/div/form/div[2]/div[2]/input""").click()
    time.sleep(.1)
    driver.find_element_by_xpath("""/html/body/div[1]/div/main/div[3]/div[1]/div/form/div[2]/div[2]/input""").send_keys(ESTIMATEEPS)
    time.sleep(.1)
    driver.find_element_by_xpath("""/html/body/div[1]/div/main/div[3]/div[1]/div/form/div[2]/div[3]/input""").click()
    time.sleep(.1)
    driver.find_element_by_xpath("""/html/body/div[1]/div/main/div[3]/div[1]/div/form/div[2]/div[3]/input""").send_keys(EPSNUMBER)
    time.sleep(.1)
    driver.find_element_by_xpath("""/html/body/div[1]/div/main/div[3]/div[1]/div/form/div[3]/input""").click()
    time.sleep(.1)
    PercentEpsBeat = driver.find_element_by_xpath("""/html/body/div[1]/div/main/div[3]/div[1]/div/form/div[6]/div/div[1]""")
    time.sleep(.1)

    elem4 = (PercentEpsBeat.text).replace('=', '')
    elem4 = elem4.replace('%', '')

    elem4 = elem4.replace("increase", '')
    elem4 = elem4.replace("decrease", '-')

    if (elem4[-1] == '-'):
        elem4 = elem4.replace("-", '')
        elem4 = '-' + elem4

    EPSchange = elem4

    #print(EPSchange)

    file1 = open("myfile.txt", "a")
    L = [EPSchange + "\n"]
    file1.writelines(L)
    file1.close()  # to change file access modes
    i = i + 1

    time.sleep(.5)
    driver.get("https://seekingalpha.com/symbol/CHWY/earnings")
    time.sleep(.5)


driver.close()