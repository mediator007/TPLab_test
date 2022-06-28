from services.site_request import get_site_title, site_check, url_transform
from services.screenshot import screenshot, time_dec
import time


def test_site_check():
    assert site_check('http://google.com') == 200
    assert site_check('bad_url') == 404


def test_get_site_title():
    assert get_site_title('http://google.com') == 'Google'
    assert site_check('bad_url') == 404


def test_url_transform():
    adress_for_req = "https://google.com"
    adresses = ["www.google.com", "https://google.com", "google.com", "http://www.google.com"]
    for adress in adresses:
        assert url_transform(adress) == adress_for_req


def test_time_dec():
    @time_dec
    def f():
        time.sleep(1)
        return 'file_name'
    res = f()
    assert (res[0], type(res[1])) == ('file_name', type(1.0))


def test_screenshot():
    file_name, time = screenshot("google.com", 123123)
    assert type(file_name) == type("")
    assert type(time) == type(1.0)