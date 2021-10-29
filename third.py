from selenium import webdriver
import time

driver=webdriver.Chrome(r"C:\Users\hp\OneDrive\Desktop\chromedriver")
# driver.maximize_window()
driver.get("https://www.instagram.com/")
time.sleep(3)
driver.find_element_by_name("username").send_keys("snuggle_peach")
time.sleep(3)
driver.find_element_by_name("password").send_keys("Nikhitha@98")
time.sleep(3)
driver.find_element_by_class_name("qF0y9").click()
time.sleep(10)
driver.find_element_by_class_name("cmbtv").click()
time.sleep(5)
driver.find_element_by_class_name("_8-yf5 ").click()
time.sleep(5)
driver.close()