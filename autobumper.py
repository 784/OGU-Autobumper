import time
from selenium import *
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Colours
CRED = '\033[91m'
CEND = '\033[0m'
CGREEN = '\33[92m'
BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'

#Credits
print(WHITE + "-------------------------------------------------------")
print(CYAN +'''
                _        _                                     
     /\        | |      | |                                    
    /  \  _   _| |_ ___ | |__  _   _ _ __ ___  _ __   ___ _ __ 
   / /\ \| | | | __/ _ \| '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
  / ____ \ |_| | || (_) | |_) | |_| | | | | | | |_) |  __/ |   
 /_/    \_\__,_|\__\___/|_.__/ \__,_|_| |_| |_| .__/ \___|_|   
                                              | |              
                                                      
''')
print(WHITE+"-------------------------------------------------------")
print(GREEN + "[-] OGU Autobumper v1")
print(GREEN + "[-] Developed by Penderdrill#0691")
print(WHITE+"-------------------------------------------------------"+ CYAN)

#Asking username, password, and thread
username = input("[+] What's your username? ")
password = input("[+] What's your password? ")
thread = input("[+] What thread do you need autobumped? ")

#Selenium things (using undetected chromedriver so Cloudflare doesn't have a seizure)
opts = uc.ChromeOptions()
opts.add_argument("--window-size=1020,900")  
driver = uc.Chrome(options=opts, use_subprocess=True, version_main=102) 

#Logging in
driver.get("https://ogu.gg/login")
email = driver.find_element(by=By.XPATH, value="/html/body/div[4]/div/form[1]/div/div[1]/div/div[2]/div/span/div[1]/span/label/input").send_keys(username)
password = driver.find_element(by=By.XPATH, value="/html/body/div[4]/div/form[1]/div/div[1]/div/div[2]/div/span/div[2]/label/input").send_keys(password)
time.sleep(2)
button = driver.find_element(by=By.XPATH, value="/html/body/div[4]/div/form[1]/div/div[1]/div/div[2]/div/span/button/span").click()

#Autobumping
while True:
    driver.get(thread)
    reply_box = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "message"))).send_keys("Autobumped using Penderdrill's autobumper!")
    post_reply = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "quick_reply_submit"))).click()
    print(GREEN + "[>] Autobumping!")
    time.sleep(1800)
    