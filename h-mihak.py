from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import time

opt=Options()
opt.add_experimental_option("debuggerAddress","localhost:8989")
opt : str= os.getcwd()+'/selenium/chromedriver.exe'
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

# 사이트 열기
driver.get("https://h-mihak.com/")

# 새로운 HTML 코드
new_html = '''
<div class="column_half map-area" id="map-container">
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3164.6389383879155!2d127.01863342614064!3d37.51643312699904!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x357ca3e9a9fb2ce5%3A0xa61513ffdf486a4f!2z7ZiE64yA66-47ZWZ7ISx7ZiV7Jm46rO8IChIeXVuZGFpIEFlc3RoZXRpY3Mp!5e0!3m2!1sko!2skr!4v1721121740087!5m2!1sko!2skr" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</div>
'''

# HTML 코드 저장 및 복원 함수
def update_map():
    # 페이지가 완전히 로드되었는지 확인
    if driver.execute_script("return document.readyState") == "complete":
        # col-12 text-center 클래스의 div 요소 찾기
        target_div = driver.find_element(By.XPATH, '//div[contains(@class, "col-12 text-center")]')
        
        # 새로운 HTML 삽입
        driver.execute_script("arguments[0].innerHTML = arguments[1];", target_div, new_html)

        # HTML 코드 저장
        driver.execute_script("localStorage.setItem('mapHTML', arguments[0]);", new_html)

        # 페이지가 로드될 때 HTML 복원
        load_script = """
            var html = localStorage.getItem('mapHTML');
            if (html) {
                var mapContainer = document.getElementById('map-container');
                if (!mapContainer) {
                    mapContainer = document.createElement('div');
                    mapContainer.id = 'map-container';
                    document.body.appendChild(mapContainer);
                }
                mapContainer.innerHTML = html;
            }
        """
        driver.execute_script(load_script)

# 무한 루프
try:
    while True:
        # 페이지가 로드된 상태인지 확인
        if driver.execute_script("return document.readyState") == "complete":
            update_map()  # 페이지가 로드된 상태일 때만 업데이트
        #time.sleep(5)  # 5초마다 체크
        time.sleep(5)
except KeyboardInterrupt:
    print("프로그램 종료")
finally:    
    driver.quit()