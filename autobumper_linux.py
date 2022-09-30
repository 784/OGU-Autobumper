import time
from datetime import datetime
import random
import os

#Automatically importing external libraries that are needed for the program to run
try:
    from selenium import *
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
except ModuleNotFoundError:   
    try:
        os.system("pip install selenium")
        from selenium import *
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
    except ModuleNotFoundError:
        print("PIP failed to install Selenium! Make sure PIP is installed on your system.")
        time.sleep(3)
        exit()
try:
    import undetected_chromedriver as uc
except ModuleNotFoundError:
    try:
        os.system("pip install undetected_chromedriver")
        import undetected_chromedriver as uc
    except ModuleNotFoundError:
        print("PIP failed to install Undetected Chromedriver! Make sure PIP is installed on your system.")
        time.sleep(3)
        exit()

#Enter your username and password here
username = ""
password = ""

#Colours
CGREEN = '\33[92m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
WHITE = '\033[37m'

#Autobump function
def autobump(thread, message = "Autobumped using Penderdrill's autobumper"):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    driver.get(thread)
    thread_message = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "message"))).send_keys(f"{message} [{str(random.randint(1000, 9999))}]") 
    reply_button = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "quick_reply_submit"))).click()     
    print(MAGENTA + f"[{current_time}] Autobump #{str(i + 1)}")
    time.sleep(7)

#Selenium things (using undetected chromedriver so Cloudflare doesn't have a seizure)
options = uc.ChromeOptions()
options.add_argument("--disable-extensions") 
options.add_argument("--start-maximized")
driver = uc.Chrome(options=options, use_subprocess=True, version_main=105) 
driver.set_page_load_timeout(2000)

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
print(BLUE + "[-] OGU Autobumper v3")
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
    
    Put the threads you want to autobump below the quotation marks (MAKE SURE TO INDENT THE AUTOBUMP FUNCTION! Spacing is important in Python)
    The thread url comes first and then the message you want to be posted onto the thread
    You can autobump as many threads as you want!
    
    """

    #Examples with a custom thread message
    autobump("https://ogu.gg/Thread-NameMC-Followers-Automated-fast-and-cheap", "Autobumping!")
    autobump("https://ogu.gg/Thread-1-PER-1000-FAST-AND-CHEAP", "Buy my credits!!")
    
    #If you don't want a custom message, just put your thread link and it'll use "Autobumped using Penderdrill's autobumper" as the message (example below)
    autobump("https://ogu.gg/Thread-NameMC-Followers-Automated-fast-and-cheap")
    
    time.sleep(1860)
