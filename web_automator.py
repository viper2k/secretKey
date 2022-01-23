from used_libraries import time, os
from selenium import webdriver # used to get the chrome driver installed
from selenium.webdriver.common.keys import Keys # used for simulating the press of the keyboard keys

def auto_login(result):
    web = webdriver.Chrome(f'C:\\Users\\{os.getlogin()}\\Desktop\\Python Password Manager in SQL\\chromedriver.exe')

    if result[3] == "https://aust.mrooms.net/login/index.php":
        web.get(result[3])
        time.sleep(1)
        login_name = result[1]
        name_field = web.find_element_by_xpath('//*[@id="username"]')
        name_field.send_keys(login_name)

        login_pass = result[2]
        pass_field = web.find_element_by_xpath('//*[@id="password"]')
        pass_field.send_keys(login_pass)

        login_field = web.find_element_by_xpath('//*[@id="loginbtn"]')
        login_field.click()
    
    if result[3] == "https://sis.aust.edu.lb/":
        web.get(result[3])
        time.sleep(1)
        login_name = result[1]
        name_field = web.find_element_by_xpath('//*[@id="username"]')
        name_field.send_keys(login_name)

        login_pass = result[2]
        pass_field = web.find_element_by_xpath('//*[@id="password"]')
        pass_field.send_keys(login_pass)

        login_field = web.find_element_by_xpath('//*[@id="ok"]')
        login_field.click()
    
    if result[3] == "https://www.facebook.com/login/":
        web.get(result[3])
        time.sleep(1)
        login_name = result[1]
        name_field = web.find_element_by_xpath('//*[@id="email"]')
        name_field.send_keys(login_name)

        login_pass = result[2]
        pass_field = web.find_element_by_xpath('//*[@id="pass"]')
        pass_field.send_keys(login_pass)

        login_field = web.find_element_by_xpath('//*[@id="loginbutton"]')
        login_field.click()
    
    if result[3] == "https://www.instagram.com/":
        web.get(result[3])
        time.sleep(1)
        login_name = result[1]
        name_field = web.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        name_field.send_keys(login_name)

        login_pass = result[2]
        pass_field = web.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        pass_field.send_keys(login_pass)

        login_field = web.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]')
        login_field.click()
    
    if result[3] == "https://twitter.com/login":
        web.get(result[3])
        time.sleep(1)
        login_name = result[1]
        name_field = web.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        name_field.send_keys(login_name)

        login_pass = result[2]
        pass_field = web.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        pass_field.send_keys(login_pass)

        login_field = web.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span')
        login_field.click()
    
    if result[3] == "https://www.reddit.com/":
        web.get(result[3])
        time.sleep(1)
        login_name = result[1]
        name_field = web.find_element_by_xpath('//*[@id="loginUsername"]')
        name_field.send_keys(login_name)

        login_pass = result[2]
        pass_field = web.find_element_by_xpath('//*[@id="loginPassword"]')
        pass_field.send_keys(login_pass)

        login_field = web.find_element_by_xpath('/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button')
        login_field.click()