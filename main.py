import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


# Test in Chrome

class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_search_chrome(self):
        driver_chrome = self.driver
        driver_chrome.get('https://spycloud.com')
        WebDriverWait(driver_chrome, 3)

        print(driver_chrome.title)
        print(driver_chrome.current_url)
        driver_chrome.find_element_by_xpath('//*[@alt="logo"]')
        print(driver_chrome.find_element(By.TAG_NAME, "img").get_attribute("src"))  # SpyCloud logo image

        #  Наведение курсора на всплывающее окно. Клик на нужный элемент.
        #  Hover the cursor over a pop-up window. Click on the desired item.

        action = ActionChains(driver_chrome)
        hidden_submenu = driver_chrome.find_element_by_xpath('//*[@id="wp-megamenu-item-13"]')
        action.move_to_element(hidden_submenu).perform()
        WebDriverWait(driver_chrome, 2)
        hidden_submenu1 = driver_chrome.find_element_by_xpath('//*[@href="/products/vip-guardian/"]')
        action.move_to_element(hidden_submenu1)
        driver_chrome.find_element_by_xpath('//*[@id = "wp-megamenu-item-20693"]').click()
        WebDriverWait(driver_chrome, 3)

        #   прокрутка страницы до искомого элемента
        #   Scroll the page to the desired element

        driver_chrome.find_element_by_xpath('//*[@class="btn btn-gradient-hover"]').send_keys(Keys.HOME)

        #   проверка текста (не работает)
        #   driver_chrome.find_element_by_xpath('//*[@class="elementor-heading-title elementor-size-default"]')
        #   assert 'Protect Your Highest-Risk Executives from Targeted Account Takeover' in driver_chrome.title
        #   print(driver_chrome.title)
        #   if not 'Protect Your Highest-Risk Executives from Targeted Account Takeover' in driver_chrome.title:
        #       raise Exception('Title is wrong')

        #  клик на нужный элемент
        #  Click on the desired item.

        driver_chrome.find_element_by_xpath('//*[@class="btn btn-gradient-hover"]').click()
        WebDriverWait(driver_chrome, 10)

        #  скрин ошибки 404
        #  404 error screen
        driver_chrome.save_screenshot(r"C:\Users\14252\Documents\QA\Test SpyCloud\Error.png")

        time.sleep(1)

    def tearDown(self):
        self.driver.quit()  # Close the browser.

# Test in Chrome (1062x722)

    def test_search_chrome_1062x722(self):
        driver_chrome = self.driver
        driver_chrome.set_window_size(1062, 722)
        driver_chrome.get('https://spycloud.com')
        WebDriverWait(driver_chrome, 3)

        print(driver_chrome.title)
        print(driver_chrome.current_url)
        driver_chrome.find_element_by_xpath('//*[@alt="logo"]')
        print(driver_chrome.find_element(By.TAG_NAME, "img").get_attribute("src"))  # SpyCloud logo image
        driver_chrome.find_element_by_xpath('//button[@id="responsive-menu-button"]').click()
        driver_chrome.find_element(By.ID, 'responsive-menu-container')
        driver_chrome.find_elements_by_xpath('//*[@class="btn btn-yellow"]')
        WebDriverWait(driver_chrome, 4)
        driver_chrome.find_elements_by_xpath('//*[@href="/check-your-exposure/"]')

        time.sleep(1)

    def tearDownClass(self):
        self.driver.quit()  # Close the browser chrome 1062x722.

# Test in Firefox


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_search_Firefox(self):
        driver_Firefox = self.driver
        driver_Firefox.get('https://spycloud.com')
        WebDriverWait(driver_Firefox, 3)

        print(driver_Firefox.title)
        print(driver_Firefox.current_url)
        driver_Firefox.find_element_by_xpath('//*[@alt="logo"]')
        print(driver_Firefox.find_element(By.TAG_NAME, "img").get_attribute("src"))  # SpyCloud logo image

        time.sleep(1)

    def tearDown(self):
        self.driver.quit()  # Close the browser Firefox.


if __name__ == "__main__":
    unittest.main()
