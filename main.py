from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from pynput.keyboard import Controller as KBController


def remove_cookie_modal():
    driver.execute_script('return document.querySelector("#qc-cmp2-main").remove()')


kbc = KBController()

driver = Chrome()
driver.get('https://www.typing.com/student/typing-test/1-minute')
remove_cookie_modal()
driver.find_element(By.TAG_NAME, 'body').send_keys('\n')
sleep(0.3)
remove_cookie_modal()

text_input = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div/div')
typing = True
while typing:
    text = text_input.text
    text = text.replace('\n', '').replace('  ', ' ')
    for c in text:
        kbc.tap(c)
        sleep(0.1)
    sleep(0.1)

driver.quit()
