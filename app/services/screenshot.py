from time import sleep
from selenium import webdriver
import os

from webdriver_manager.chrome import ChromeDriverManager

url = "https://github.com"

# driver = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Chrome('/home/viktor/Desktop/TPLab_test/app/services/chromedriver')

def screenshot(url):
    driver.get(url)
    sleep(3)
    driver.get_screenshot_as_file(f"./media/github.png")
    driver.quit()

if __name__=="__main__":
    screenshot(url)