import time
from selenium import webdriver

driver = webdriver.Chrome('/home/viktor/Desktop/TPLab_test/app/services/chromedriver')

def time_dec(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        t = t2 - t1
        print(t)
        return res
    return wrapper

@time_dec
def screenshot(url: str):
    driver.get(url)
    time.sleep(3)
    driver.get_screenshot_as_file(f"./media/github.png")
    driver.quit()

# if __name__=="__main__":
#     screenshot('http://google.com')