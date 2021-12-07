from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def sum(first_number, second_number):
    """
    Returns string sum of two integers passed as strings
    """
    return str(int(first_number) + int(second_number))


def main(link):
    browser = webdriver.Chrome('../chromedriver')
    browser.get(link)

    first_number = browser.find_element_by_id("num1")
    second_number = browser.find_element_by_id("num2")

    result = sum(first_number.text, second_number.text)

    dropdown = Select(browser.find_element_by_id("dropdown"))
    dropdown.select_by_value(result)

    submit = browser.find_element_by_tag_name("button")
    submit.click()

    sleep(10)
    browser.quit()


if __name__ == "__main__":
    link = "http://suninjuly.github.io/selects2.html"
    main(link)
