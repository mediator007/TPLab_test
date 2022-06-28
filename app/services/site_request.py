import requests
from lxml.html import fromstring
from loguru import logger


def url_transform(url):
    """
    Transfor url for request
    """
    url_special = url.replace('http://', '').replace("https://", '').replace('www.', '')
    url_for_request = "http://" + url_special
    return url_for_request


def site_check(url):
    """
    Get response status code by URL
    """
    try:
        url_for_request = url_transform(url)
        logger.info(f"request: {url_for_request}")
        response = requests.get(url_for_request)
        return int(response.status_code)
    except Exception as e:
        logger.warning(f"Bad URL: {url}")
        return 404


def get_site_title(url):
    """
    Get site title by URL
    """
    url_for_request = url_transform(url)
    response = requests.get(url_for_request)
    tree = fromstring(response.content)
    title = tree.findtext('.//title')
    return title
