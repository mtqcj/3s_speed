import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
chrome_options = Options()
import random
import time

domain_list = list()
fd = open("domain.txt", "r")

for i in fd.read().split("\n"):
    #url = 'window.open("https://' + i + '")'
    url ="https://"+i
    domain_list.append(url)

while True:

    chrome_options.add_argument("--user-data-dir=" + r"C:/Users/sun/AppData/Local/Google/Chrome/User Data")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    for i in domain_list:
        driver.get(i)
        #time.sleep(5)
        print(i)
        time.sleep(10)
    driver.quit()

