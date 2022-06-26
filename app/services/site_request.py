import requests
from lxml.html import fromstring
from loguru import logger


def site_check(url):
    """
    Get response status code by URL
    """
    try:
        response = requests.get(url)
        return int(response.status_code)
    except Exception as e:
        logger.warning(f"Bad URL: {url}")
        return 404


def get_site_title(url):
    """
    Get site title by URL
    """
    response = requests.get(url)
    tree = fromstring(response.content)
    title = tree.findtext('.//title')
    return title
