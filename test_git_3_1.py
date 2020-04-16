from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    element = browser.find_element_by_id("input_value") 
    time.sleep(1)
    x = element.text
    y = calc(x) 
    
    
    browser.execute_script("window.scrollBy(0, 120);")
    
    input1 = browser.find_element_by_class_name("form-control")
    input1.send_keys(y)
    
    
    
    select1 = browser.find_element_by_id("robotCheckbox")
    select1.click()
    
    select2 = browser.find_element_by_id("robotsRule")
    select2.click()
    
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()
    
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()