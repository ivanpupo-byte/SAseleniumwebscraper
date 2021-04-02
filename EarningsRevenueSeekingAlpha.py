from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key, Controller
import time
from bs4 import BeautifulSoup
import bs4 as bs
from selenium.common.exceptions import NoSuchElementException
import re

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

    REVENUE = driver.find_element_by_xpath("""/html/body/div[3]/div[1]/div/div/div/div/div[2]/div/section[6]/div[2]/div["""+row+"""]/div[1]/div/a/span[3]""")

    REVENUETEXT = REVENUE.text

    REVENUETEXT = REVENUETEXT.replace("Revenue", '')

    # print(REVENUETEXT)

    REVENUESPLIT = REVENUETEXT.split("e")

    # print(REVENUESPLIT[0])
    # print(REVENUESPLIT[1])

    REVENUETEXT = re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", REVENUESPLIT[0])

    # print(REVENUETEXT)

    REVENUETEXT = REVENUETEXT.replace("()", '')
    REVENUETEXT = REVENUETEXT.replace("b", '')
    REVENUETEXT = REVENUETEXT.replace("miss", '')
    REVENUETEXT = REVENUETEXT.replace("of", '')
    REVENUETEXT = REVENUETEXT.replace("$", '')
    REVENUETEXT = REVENUETEXT.replace("M", '0000')
    REVENUETEXT = REVENUETEXT.replace("B", '0000000')
    REVENUETEXT = REVENUETEXT.replace("K", '')
    REVENUETEXT = REVENUETEXT.replace(" ", '')
    REVENUETEXT = REVENUETEXT.replace(".", '')

    # print(REVENUETEXT)

    REVENUEBEAT = REVENUESPLIT[1]

    REVENUEBEAT = REVENUEBEAT.replace("at", '')
    REVENUEBEAT = REVENUEBEAT.replace("d", '')
    REVENUEBEAT = REVENUEBEAT.replace("by", '')
    REVENUEBEAT = REVENUEBEAT.replace("$", '')
    REVENUEBEAT = REVENUEBEAT.replace("M", '0000')
    REVENUEBEAT = REVENUEBEAT.replace("B", '0000000')
    REVENUEBEAT = REVENUEBEAT.replace("K", '')
    REVENUEBEAT = REVENUEBEAT.replace(" ", '')
    REVENUEBEAT = REVENUEBEAT.replace(".", '')

    # print(REVENUEBEAT)

    REVENUEFLOAT = float(REVENUETEXT)
    REVENUEBEATFLOAT = float(REVENUEBEAT)

    ESTIMATEDREVENUE = REVENUEFLOAT - REVENUEBEATFLOAT

    ESTIMATEDREVENUE = str(ESTIMATEDREVENUE)

    #print(ESTIMATEDREVENUE)

    driver.get("https://www.calculatorsoup.com/calculators/algebra/percent-change-calculator.php")
    time.sleep(1)
    driver.find_element_by_xpath("""/html/body/div[1]/div/main/div[3]/div[1]/div/form/div[2]/div[2]/input""").click()
    time.sleep(.1)
    driver.find_element_by_xpath("""/html/body/div[1]/div/main/div[3]/div[1]/div/form/div[2]/div[2]/input""").send_keys(ESTIMATEDREVENUE)
    time.sleep(.1)
    driver.find_element_by_xpath("""/html/body/div[1]/div/main/div[3]/div[1]/div/form/div[2]/div[3]/input""").click()
    time.sleep(.1)
    driver.find_element_by_xpath("""/html/body/div[1]/div/main/div[3]/div[1]/div/form/div[2]/div[3]/input""").send_keys(REVENUETEXT)
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