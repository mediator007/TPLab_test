import time
from datetime import datetime
from async_timeout import timeout
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from loguru import logger

from services.site_request import url_transform

def time_dec(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        file_name = func(*args, **kwargs)
        t2 = time.time()
        t = t2 - t1
        return file_name, t
    return wrapper

@time_dec
def screenshot(url: str, user_id: str) -> str:
    """
    Запись скриншота в файл
    """
    driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
    # driver = webdriver.Chrome("/home/viktor/Desktop/TPLab_test/app/services/chromedriver")
    try:

        logger.info("driver up")
        time.sleep(2)
        current_date = datetime.now()
        format_date = current_date.strftime("%d_%m_%Y")
        format_url_for_file= url.replace('.', '_').replace('http://', '').replace('www.', '')
        url_for_request = url_transform(url)
        file_name = (f'./app/services/media/{format_date}_{user_id}_{format_url_for_file}.png')
        driver.get(url_for_request)
        logger.info(f"get url: {url_for_request}")
        time.sleep(2)
        driver.get_screenshot_as_file(filename=file_name)
        logger.info(f"get screenshot name: {file_name}")
    finally:
        driver.quit()
        return file_name
