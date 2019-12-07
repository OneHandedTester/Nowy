from Selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximimize_window()
driver.get("http://www.google.pl")
driver.find_element_by_name('q')

pole_wyszukiwania.send_keys("tester CDV")
clear()


time.sleep(0.4)
driver.close()
