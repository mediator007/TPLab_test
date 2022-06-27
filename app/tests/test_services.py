from services.site_request import get_site_title, site_check
from services.screenshot import screenshot, time_dec
import time


def test_site_check():
    assert site_check('http://google.com') == 200
    assert site_check('bad_url') == 404


def test_get_site_title():
    assert get_site_title('http://google.com') == 'Google'
    assert site_check('bad_url') == 404


def test_screenshot():
    ...


def test_time_dec():
    @time_dec
    def f():
        time.sleep(1)
        return 'file_name'
    res = f()
    assert (res[0], type(res[1])) == ('file_name', type(1.0))