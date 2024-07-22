from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from EbayProduct import ebaySell
import pandas as pd
import json
import requests
import os
from selenium.webdriver.chrome.options import Options
options=Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-web-security')  
options.add_argument('--disable-dev-shm-usage')  
options.add_argument('--no-sandbox')

driver=webdriver.Chrome(options=options)

url = "https://www.amazon.in/"
driver.maximize_window()
driver.get(url)

search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
)

search_box.send_keys("laptop")
search_box.submit()

# # # Wait for the initial set of elements to load
WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "s-result-item"))
)

# # # Fetch all the product URLs on the search page
product_links = driver.find_elements(
    By.XPATH, '//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]/a'
)

# # # Store the URLs in a list
urls_to_visit = [
    link.get_attribute("href") for link in product_links if link.get_attribute("href")
]
product_url = urls_to_visit[0]


def get_product_data(url):
    try:
        all_data = []
        driver.get(url)
        product_title = (
            WebDriverWait(driver, 20)
            .until(EC.presence_of_element_located((By.ID, "productTitle")))
            .text
        )
        product_price = (
            WebDriverWait(driver, 20)
            .until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "reinventPricePriceToPayMargin")
                )
            )
            .text
        )
        # # product img
        product_image = (
            WebDriverWait(driver, 20)
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, "#landingImage")))
            .get_attribute("src")
        )
        # get all the product details
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#poToggleButton > a"))
        ).click()
        keys = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "td.a-span3"))
        )

        values = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "td.a-span9"))
        )  # feature-bullets > ul > li:nth-child(1) > span
        # product about
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#feature-bullets > div > a"))
        ).click()
        product_abouts = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "#feature-bullets > ul > li.a-spacing-mini")
            )
        )
        product_about = [i.text for i in product_abouts]
        feature_name = None
        feature_value = None

        for k in range(len(keys)):
            feature_name = keys[k].text
            feature_value =values[k].text
        # product_video_click = (
        #     WebDriverWait(driver, 20)
        #     .until(
        #         EC.element_to_be_clickable(
        #             (By.XPATH, "//*[@id='a-autoid-10']/span/input")
        #         )
        #     )
        #     .click()
        # )
    #     # FOR ALL VIDEO URLS
    #     product_video_class = WebDriverWait(driver, 10).until(
    #     EC.presence_of_all_elements_located((By.XPATH, '//*[@id="anonCarousel8"]/ol/li/a'))
    # )
    #     for element in product_video_class:
    
    #         product_video = element.find_element(By.TAG_NAME, 'a').get_attribute('href')

        # time.sleep(10)
        all_data.append(
            {
                "product_title": product_title,
                "product_price": product_price,
                "product_image": product_image,
                "product_about": product_about,
                feature_name: feature_value,
            }
        )
        driver.quit()
        return all_data

    except Exception as e:
        print(f"Error occurred while fetching data from {url}: {e}")
# image
    # image_url = product_image
    # image_response = requests.get(image_url)
    # image_filename = 'product_image.jpg'
    # image_path = os.path.join(os.getcwd(), image_filename)
    # with open(image_path, 'wb') as image_file:
    #     image_file.write(image_response.content)   
#video file
    # video_url = product_video
    # video_response = requests.get(video_url)
    # video_filename = 'product_video.mp4'
    # video_path = os.path.join(os.getcwd(), video_filename)
    # with open(video_path, 'wb') as video_file:
    #     video_file.write(video_response.content)

# # Iterate through each URL and fetch data
# for product_url in urls_to_visit:
#     get_product_data(driver, product_url)
get_product_data(product_url)
ebaySell(driver)
