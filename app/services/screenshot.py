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
        current_date = datetime.now()
        # fix date format for file name
        format_date = current_date.strftime("%d_%m_%Y")
        # format url for request
        format_url_for_file= url.replace('.', '_').replace('http://', '').replace('www.', '')
        url_for_request = url_transform(url)
        # generate file name and path for saving
        file_name = (f'./app/services/media/{format_date}_{user_id}_{format_url_for_file}.png')
        # open browser

        # TRY: driver.set_page_load_timeout(30)

        
        driver.get(url_for_request)
        time.sleep(2)
        logger.info(f"get url: {url_for_request}")
        # make screenshot and save to path from file_name
        driver.get_screenshot_as_file(filename=file_name) # try: get_screenshot(filename=file_name)
        logger.info(f"get screenshot name: {file_name}")
    except Exception as e:
        logger.error(f"{e} in screenshot {url_for_request}")
    finally:
        driver.quit()
        return file_name