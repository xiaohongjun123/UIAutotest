
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from selenium import webdriver
from PIL import Image
import time
from selenium.webdriver.chrome.options import Options


def ScreenPic():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--mute-audio")
    options.add_argument('window-size=1600x1100')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    #prefs = {"profile.managed_default_content_settings.images": 2}
    #options.add_experimental_option("prefs", prefs)

    options.add_argument("--headless")
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path="/opt/google/chrome/chromedriver", options=options)
    driver.fullscreen_window()
    #print(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/testreport/UIAutoTestReport.html")
    driver.get("file:///home/xiaohongjun/uitest/testreport/UIAutoTestReport.html")
    filename = "Screemshot.png"
    time.sleep(3)
    driver.save_screenshot(filename)
    ele = driver.find_element_by_xpath('''/html/body/div[2]/div[1]/div''')
    left = ele.location["x"]
    top = ele.location["y"]
    right = left + ele.size["width"]
    bottom = top + ele.size["height"]
    im = Image.open(filename)
    im1 = im.crop((left, top, right, bottom))
    print(im1)
    im1.save(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/testreport/"+filename)
    driver.quit()


if __name__=="__main__":
    ScreenPic()