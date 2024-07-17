from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import time

xpath = '//a[@class="link_login"]' # '//태그[@속성="속성값"]' 형식으로 xpath 구성
xpath2 = '//input[@id="id"]'
xpath3 = '//input[@id="pw"]'
xpath4 = '//input[@id="log.login"]'

opt=Options()
opt.add_experimental_option("debuggerAddress","localhost:8989")
opt : str= os.getcwd()+'/selenium/chromedriver.exe'
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

# 사이트 열기
driver.get("https://h-mihak.com/")

# 대기
#time.sleep(2)

# 원하는 div를 찾고 HTML 코드 삽입
new_html = '''
<div class="column_half map-area">
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3164.6389383879155!2d127.01863342614064!3d37.51643312699904!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x357ca3e9a9fb2ce5%3A0xa61513ffdf486a4f!2z7ZiE64yA66-47ZWZ7ISx7ZiV7Jm46rO8IChIeXVuZGFpIEFlc3RoZXRpY3Mp!5e0!3m2!1sko!2skr!4v1721121740087!5m2!1sko!2skr" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</div>
'''

# col-12 text-center 클래스의 div 요소 찾기
target_div = driver.find_element(By.XPATH, '//div[contains(@class, "col-12 text-center")]')

# 새로운 HTML 삽입
driver.execute_script("arguments[0].innerHTML = arguments[1];", target_div, new_html)

# 대기 후 종료
time.sleep(10000000)
driver.close()
driver.quit()
