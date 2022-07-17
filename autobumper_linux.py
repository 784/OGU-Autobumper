import time
from selenium import *
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

#Colours
CGREEN = '\33[92m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
WHITE   = '\033[37m'

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

#Enter your username, password, and the thread you want bumped here!
username = ""
password = ""
thread = ""

#Selenium things (using undetected chromedriver so Cloudflare doesn't have a seizure)
options = uc.ChromeOptions()
options.add_argument("--disable-extensions") 
options.add_argument("--start-maximized")
driver = uc.Chrome(options=options, use_subprocess=True, version_main=104) 

#Logging in
driver.get("https://ogu.gg/login")
email = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/form[1]/div/div[1]/div/div[2]/div/span/div[1]/span/label/input"))).send_keys(username)
password = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/form[1]/div/div[1]/div/div[2]/div/span/div[2]/label/input"))).send_keys(password)
button = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/form[1]/div/div[1]/div/div[2]/div/span/button/span"))).click()

#Autobumping every 31 minutes
for i in range(100000000):

    #Finding current date and time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    #Doing the actual bumping
    driver.get(thread)
    reply_box = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "message"))).send_keys("Bumping! https://discord.gg/gPTU7zq3br Contact me on discord for a faster response :D")
    post_reply = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "quick_reply_submit"))).click()  
    print(MAGENTA + f"[{current_time}] Autobump #" + str(i + 1))
    driver.set_page_load_timeout(1000)
    time.sleep(1860)    
    
