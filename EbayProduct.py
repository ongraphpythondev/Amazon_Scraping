from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import os
def ebaySell(driver):
    url = "https://www.ebay.com/"
    driver.maximize_window()
    driver.get(url)
    sellButton = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='gh-p-2']/a"))
    )
    sellButton.click()
    button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div/div[2]/nav/ul/li[3]/a"))
    ).click()
    button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div/div[2]/nav/ul/li[6]/a"))
    ).click()
    WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.ID, "s0-1-1-24-7-@keyword-@box-@input-textbox"))).send_keys("bag")
    WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.ID, "s0-1-1-24-7-@keyword-@box-@input-textbox"))).send_keys(Keys.RETURN)

    WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mainContent"]/div/div/div[2]/button'))).click()

    radio_buttons = driver.find_elements(By.CLASS_NAME, "radio__control")
    radio_buttons[0].click()

    WebDriverWait(driver,40).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='mainContent']/div/div/div[1]/div[1]/div/div[2]/div[3]/div/div/div[2]/button"))
    ).click()

    WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="signin_ggl_btn"]'))).click()
    WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="identifierId"]'))).send_keys("test@gmail.com")
    WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span'))).click()

    password_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="password"]'))
    )
    password_input.send_keys("test1234")
    WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button'))).click()


    WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="countryId"]/option[94]'))).click()

    sleep(2)
    WebDriverWait(driver,40).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'#address1'))).send_keys("Meerut")
    WebDriverWait(driver,40).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#address2')) ).send_keys("santivhiar")
    WebDriverWait(driver,40).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#city')) ).send_keys("Meerut")
    WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="state"]/option[36]'))).click()
    WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="zip"]'))).send_keys("pincode")
    sleep(2)
    WebDriverWait(driver,40).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="phoneFlagComp1"]'))
    ).send_keys("123456789")
    sleep(3)
    WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#country-listphoneFlagComp1 > li:nth-child(94)'))).click()
    sleep(2)
    WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="sbtBtn"]'))).click()
    sleep(2)
    WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mainContent"]/div/div/div[1]/div[2]/div[2]/div[2]/button'))).click()
    WebDriverWait(driver,40).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="mainContent"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/button[1]'))).send_keys(os.getcwd()+"/home/ongraph/Desktop/amozone_scraping/product_image.jpg")
    sleep(2)
