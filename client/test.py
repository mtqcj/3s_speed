import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
chrome_options = Options()
import random
import time


chrome_options.add_argument("--user-data-dir="+r"C:/Users/sun/AppData/Local/Google/Chrome/User Data/")
#driver = webdriver.Chrome(chrome_options=chrome_options)

def run(test):
    driver = webdriver.Chrome(chrome_options=chrome_options)
    #driver = webdriver.Chrome(chrome_options=chrome_options)
    driver .execute_script(test)
    time.sleep(5)
    driver.close()


domain_set=set()
fd=open("domain.txt","r")

for i in fd.read().split("\n"):
    url='window.open("https://'+i+'")'
    domain_set.add(url)
    #print(url)

slice = random.sample(domain_set, 2)
print(slice,type(slice))


while True:
    chrome_options.add_argument("--user-data-dir="+r"C:/Users/sun/AppData/Local/Google/Chrome/User Data/")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    for i in slice:
        #run(i)
        driver .execute_script(i)
        
        #driver.close()
    #browser = webdriver.Chrome(chrome_options=chrome_options)
    #driver.close    
    time.sleep(10)    
    driver.quit()
