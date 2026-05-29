from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("http://localhost:3000")

time.sleep(5)

map_element = driver.find_element(By.ID, "map")

print("Mapa encontrado correctamente")

time.sleep(5)

driver.quit()