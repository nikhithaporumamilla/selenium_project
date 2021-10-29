from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Users\hp\OneDrive\Desktop\chromedriver")

driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(3)
driver.find_element_by_id("email").send_keys("nikhithaporumamilla@gmail.com")

time.sleep(3)
driver.find_element_by_id("pass").send_keys("Nikhitha@98")
time.sleep(3)
driver.find_element_by_class_name("sqdOP").click()
time.sleep(15)
driver.close()
