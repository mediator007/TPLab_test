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
def screenshot(url: str, user_id: str):
    current_date = datetime.now()
    format_current_date = current_date.strftime("%d_%m_%Y")
    file_name = ("./media/url.png")
    driver = webdriver.Chrome('/home/viktor/Desktop/TPLab_test/app/services/chromedriver')
    driver.get(url)
    time.sleep(3)
    driver.get_screenshot_as_file(
        filename=f'/home/viktor/Desktop/TPLab_test/app/services/media/{1}url.png'
        )
    driver.quit()
    return file_name

# if __name__=="__main__":
#     res, t = screenshot('http://google.com', 234)
#     print(t)