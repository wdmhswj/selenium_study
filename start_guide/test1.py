from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
 
# s = Service("D:\Apps\chromedriver-win64\chromedriver.exe")  # 存储驱动所在路径
# d = webdriver.Chrome(service=s)  # 从路径提取驱动,设置驱动名为d
# d.implicitly_wait(60)  # 设置每个步骤最大等待时间
# d.get('https://www.baidu.com')  # GET方法访问百度

options = webdriver.ChromeOptions()
options.add_argument('--enable-chrome-browser-cloud-management')
options.add_argument('--no-sandbox')
# options.add_experimental_option('detach', True)


def test_eight_components():
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    driver.quit()


if __name__ == "__main__":
    test_eight_components()