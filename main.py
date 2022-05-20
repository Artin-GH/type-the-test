from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep
from pynput.keyboard import Controller as KBController

kbc = KBController()

chrome = Chrome()
chrome.get('https://www.typing.com/student/login')
chrome.find_element(By.CSS_SELECTOR, '#form-ele-username').send_keys('<username>')
chrome.execute_script('document.querySelector("#form-ele-password").value = "<password>"')
nxt = chrome.find_element(By.XPATH, '//*[@id="app"]/div/div/main/div/div[4]/div[2]/div[2]/div[2]/button')
try:
    nxt.click()
except ElementClickInterceptedException:
    chrome.find_element(By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]').click()
    nxt.click()
sleep(3)
nxt.click()
del nxt
sleep(2)
chrome.get('https://www.typing.com/student/typing-test/1-minute')
typing = True
while typing:
    txt = chrome.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div/div').text
    txt = txt.replace('\n', '').replace('  ', ' ')
    for c in txt:
        kbc.tap(c)
        sleep(0.1)
    sleep(0.1)
