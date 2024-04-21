from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建驱动程序实例
driver = webdriver.Chrome()

# 在浏览器上执行操作
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

#  请求 浏览器信息 
title = driver.title

# 建立等待策略
driver.implicitly_wait(0.5)

#  发送命令 查找元素 
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# 操作元素
text_box.send_keys("Selenium")
submit_button.click()

# 获取元素信息
message = driver.find_element(by=By.ID, value="message")
text = message.text

# 退出
driver.quit()