#  -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

# Initialize the webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)


def tv():
    driver.get("https://www.amazon.com/TVs/s?k=TVs")
    time.sleep(5)
    print("-----  TV site  -----")
    for i in range(1, 3):
        items = driver.find_elements(
            By.CSS_SELECTOR, "div.s-result-list.s-search-results div.s-result-item"
        )
        num_items = len(items)
        for j in range(1, num_items):
            try:
                product = (
                    items[j]
                    .find_element(By.CSS_SELECTOR, "h2.a-size-mini a.s-underline-text")
                    .text
                )
                image = (
                    items[j]
                    .find_element(By.CSS_SELECTOR, "img.s-image")
                    .get_attribute("src")
                )
                link = (
                    items[j]
                    .find_element(By.CSS_SELECTOR, "h2.a-size-mini a.s-underline-text")
                    .get_attribute("href")
                )
                try:
                    prices = items[j].find_elements(By.CSS_SELECTOR, "span.a-price")
                    price_1 = prices[0].text
                    try:
                        price_2 = prices[1].text
                    except:
                        price_2 = ""
                except:
                    price_1 = ""
                    price_2 = ""

                data = [[product, image, price_1, price_2, link]]

                with open("tvs.csv", "a", encoding="utf-8", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(data)
                print(f"{j} item scraped.")
            except:
                pass
        print(f"{i} page completed")
        next_button = driver.find_element(By.CSS_SELECTOR, "a.s-pagination-next")
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(10)


def main():
    tv()
    time.sleep(3)


if __name__ == "__main__":
    main()
driver.quit()
