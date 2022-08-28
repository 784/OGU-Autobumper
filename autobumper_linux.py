import time
from selenium import *
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from random import choice

#Enter your username and password here (it's needed so you're able to login and post the autobump message)
username = ""
password = ""

#Colours
CGREEN = '\33[92m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
WHITE = '\033[37m'

#Selenium things (using undetected chromedriver so Cloudflare doesn't have a seizure)
options = uc.ChromeOptions()
options.add_argument("--disable-extensions") 
options.add_argument("--start-maximized")
driver = uc.Chrome(options=options, use_subprocess=True, version_main=105) 
driver.set_page_load_timeout(2000)

#Autobump a thread
def autobump(thread, message):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    driver.get(thread)
    thread_message = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "message"))).send_keys(f"{message} #{str(i + 1)}") 
    reply_button = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "quick_reply_submit"))).click()     
    print(MAGENTA + f"[{current_time}] Autobump #{str(i + 1)}")
    time.sleep(7)

#Credits
print(WHITE + "-----------------------------------------------------------------------")
print(CGREEN +'''
 .d88888b.   .d8888b.  888     888 
d88P" "Y88b d88P  Y88b 888     888 
888     888 888    888 888     888 
888     888 888        888     888 
888     888 888  88888 888     888 
888     888 888    888 888     888 
Y88b. .d88P Y88b  d88P Y88b. .d88P 
 "Y88888P"   "Y8888P88  "Y88888P"                                                        
''')
print(WHITE + "-----------------------------------------------------------------------")
print(BLUE + "[-] OGU Autobumper v2")
print(BLUE + "[-] Developed by Penderdrill#0691")
print(WHITE + "-----------------------------------------------------------------------")

#Logging in
driver.get("https://ogu.gg/login")
email = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/form[1]/div/div[1]/div/div[2]/div/span/div[1]/span/label/input"))).send_keys(username)
password = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/form[1]/div/div[1]/div/div[2]/div/span/div[2]/label/input"))).send_keys(password)
button = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/form[1]/div/div[1]/div/div[2]/div/span/button"))).click()
time.sleep(5)

#Autobumping every 31 minutes
for i in range(100000000):

    """
    
    Put the threads you want to autobump here
    The thread url comes first and then the message you want to be posted onto the thread
    You can autobump as many threads as you want!
    
    """

    #Examples
    autobump("https://ogu.gg/Thread-NameMC-Followers-Automated-fast-and-cheap", "Autobumping!")
    autobump("https://ogu.gg/Thread-1-PER-1000-FAST-AND-CHEAP", "Buy my credits!!")

    time.sleep(1860)
    
