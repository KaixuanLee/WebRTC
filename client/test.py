from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
 
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu') 
# options.add_argument('--window-size=1920x1080')
# options.add_argument('--remote-debugging-port=9222')

ch_option = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values.notifications': 2,
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1  
}
ch_option.add_experimental_option('prefs', prefs)
ch_option.add_experimental_option('excludeSwitches', ['enable-automation'])
ch_option.add_argument('--ignore-certificate-errors')
# ch_option.add_argument('--use-fake-device-for-media-stream')
# ch_option.add_argument('--use-fake-ui-for-media-stream')  
# ch_option.add_argument('--headless')
# ch_option.add_argument('--disable-gpu')

 
browser = webdriver.Chrome(options = ch_option)
browser.get('https://localhost:8443/')


# browser.find_element_by_id('kw').send_keys('HELLO')
sleep(5)
browser.find_element_by_id('start').click()
 
sleep(10)   
browser.save_screenshot('chrome-headless-test.png')