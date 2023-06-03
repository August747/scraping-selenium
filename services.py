import time

from selenium.webdriver.common import keys

import config

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class SocialNetworkScraper:
    BASE_URL = f'http://{config.SOCIAL_NETWORK_HOST}:{config.SOCIAL_NETWORK_PORT}'
    LOGIN_URL = f'{BASE_URL}/auth/login'
    BLOG_URL = f'{BASE_URL}/user/blog'
    REGISTER_URL = f'{BASE_URL}/auth/register'

    def __init__(self):
        self.driver = None

    def create_driver(self):
        try:
            self.driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)
            return self.driver
        except Exception as e:
            print(e.args)

    def social_network_register(self):
        driver = self.create_driver()
        driver.get(self.REGISTER_URL)

        username_reg_elem = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='username']")
        username_reg_elem.send_keys(config.SOCIAL_NETWORK_LOGIN)

        username_email = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='email']")
        username_email.send_keys(config.SOCIAL_NETWORK_LOGIN_EMAIL)

        username_password = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='password']")
        username_password.send_keys(config.SOCIAL_NETWORK_PASSWORD)

        username_password = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='confirm_password']")
        username_password.send_keys(config.SOCIAL_NETWORK_PASSWORD)

        username_first_name = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='first_name']")
        username_first_name.send_keys(config.SOCIAL_NETWORK_FIRST_NAME)

        username_last_name = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='last_name']")
        username_last_name.send_keys(config.SOCIAL_NETWORK_LAST_NAME)

        username_linkedin = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='linkedin_url']")
        username_linkedin.send_keys(config.SOCIAL_NETWORK_LINKEDIN)

        username_facebook = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='facebook_url']")
        username_facebook.send_keys(config.SOCIAL_NETWORK_FACEBOOK)
        username_facebook.send_keys(keys.Keys.ENTER)

    def social_network_login(self):
        driver = self.create_driver()
        self.driver.get(self.LOGIN_URL)

        username_elem = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='username']")
        username_elem.send_keys(config.SOCIAL_NETWORK_LOGIN)

        password_elem = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='password']")
        password_elem.send_keys(config.SOCIAL_NETWORK_PASSWORD)
        password_elem.send_keys(keys.Keys.ENTER)

        return driver

    def social_network_add_post(self, title, content, login_required=True):
        if login_required:
            self.driver = self.social_network_login()

        self.driver.get(self.BLOG_URL)
        time.sleep(1)

        title_elem = self.driver.find_element(By.ID, "title")
        title_elem.send_keys(title)
        time.sleep(1)

        content_elem = self.driver.find_element(By.ID, "content")
        content_elem.send_keys(content)
        time.sleep(1)

        content_elem = self.driver.find_element(By.ID, "content")
        content_elem.send_keys(content)

        create_post_elem = self.driver.find_element(By.XPATH, "//form/button[@type='submit']")
        create_post_elem.click()
        time.sleep(1)

        like_post_elem = self.driver.find_element(By.XPATH, "//a[contains( @class , 'btn-outline-primary') and "
                                                            "contains(., like)]")
        like_post_elem.click()
        time.sleep(2)

    def logout(self, login_required=True):
        if login_required:
            self.driver = self.social_network_login()

        logout_elem = self.driver.find_element(By.XPATH, "//a[@href='/auth/logout']")
        logout_elem.click()


