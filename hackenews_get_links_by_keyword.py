__doc__ = """
Get all the links has been voted the most by keyword on Hackernews 

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_result(url):
    browser = webdriver.Firefox()
    browser.get(url)
    # searching for the search box by class name
    search = browser.find_element_by_class_name("SearchInput")
    time.sleep(1)
    # input keyword "sql" into the search box
    search.send_keys("sql")
    # hit enter
    search.send_keys(Keys.RETURN)
    # excute an explicit wait
    try:
        search_container = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "SearchResults_container")))
        time.sleep(2)
        print(search_container.text)

    finally:
        browser.quit()


def main():
    url = "https://hn.algolia.com/"
    return get_result(url)


if __name__ == "__main__":
    main()
