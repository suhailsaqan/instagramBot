from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import random

class InstaBot:
    def __init__(self, username, pw):
        self.opts = Options()
        self.opts.add_argument("user-agent='hi'")
        
        self.driver = webdriver.Chrome(r"C:\Users\suhai\OneDrive\Documents\chromedriver.exe", chrome_options=self.opts)
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]')\
            .click()
        sleep(4)
        self.automate_liking()
        
    def automate_liking(self):
        self.count = 0
        while True:
            self.rand_scroll()
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/div/div[1]/div[2]/div/a/div/div[2]')\
                .click()
            sleep(1.5)
            try:
                self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]')\
                .click()
            except Exception as e:
                print(e)
            self.driver.find_element_by_xpath('/html/body/div[4]/div[3]')\
                .click()
            sleep(1)
            self.count = self.count + 1
            print(self.count)
        
    def rand_scroll(self):
        self.random = random
        value = self.random.choice([0, 1, 2, 3, 4,5,6,7,8,9,10])
        print('Random Scroll is: ', value)
        for i in range(0, value):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
my_bot = InstaBot(account, password)