from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

ch = Options()
ch.add_argument("--remote-allow-origins=*")
driver = webdriver.Chrome(options= ch)
driver.maximize_window()
action = ActionChains(driver)
driver.get("https://webdriveruniversity.com/Actions/index.html#")
time.sleep(3)

click = driver.find_element(By.XPATH,"//div[@id='click-box']")
action.click_and_hold(click).perform()
time.sleep(3)

click2 = driver.find_element(By.XPATH,"//div[@id='double-click']")
action.double_click(click2).perform()
time.sleep(3)

drag = driver.find_element(By.XPATH,"//b[text()='DRAG ME TO MY TARGET!']")
drop = driver.find_element(By.XPATH,"//div[@id='droppable']")
action.drag_and_drop(drag,drop).perform()
time.sleep(3)

hover = driver.find_element(By.XPATH," //button[text()='Hover Over Me First!']")
action.move_to_element(hover).perform()
time.sleep(3)
h1 = driver.find_element(By.XPATH,"//div[@class='dropdown hover']/div/a")
h1.click()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(3)