import time
from datetime import datetime
from selenium import webdriver


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
    current_date = datetime.now()
    format_date = current_date.strftime("%d_%m_%Y")
    format_url = url.replace('.', '_').replace('http://', '')
    file_name = (
        f'./app/services/media/{format_date}_{user_id}_{format_url}.png'
        )
    driver = webdriver.Chrome('./app/services/chromedriver')
    driver.get(url)
    time.sleep(3)
    driver.get_screenshot_as_file(filename=file_name)
    driver.quit()
    return file_name