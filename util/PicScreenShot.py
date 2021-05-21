
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from selenium import webdriver
from PIL import Image
import time
from selenium.webdriver.chrome.options import Options
from util import ProjectPath


def ScreenPic(url,screenshot_name,screenshot_path):
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--mute-audio")
    options.add_argument('window-size=1920x3000')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument("--headless")
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path="/opt/google/chrome/chromedriver", options=options)
    driver.fullscreen_window()

    
    driver.get("file://"+url)#window不需要"file://"
    time.sleep(2)
    driver.save_screenshot(screenshot_name)
    ele = driver.find_element_by_xpath('''/html/body/div[2]/div[1]/div''')
    left = ele.location["x"]
    top = ele.location["y"]
    print(ele.location)
    right = left + ele.size["width"]
    bottom = top + ele.size["height"]
    print(ele.size)
    im = Image.open(screenshot_name)
    im1 = im.crop((left, top, right, bottom))
    im1.save(screenshot_path)

def ScreenPicTwo():
    url_two=ProjectPath.PtPath("/testreport/UIAutoTestReport_two.html")
    screenshot_name = "screenshot_two.png"
    screenshot_path = ProjectPath.PtPath("/testreport/" + screenshot_name)
    if os.path.exists(url_two)==True:
        ScreenPic(url_two,screenshot_name,screenshot_path)
    else:
        pass
    return url_two,screenshot_path


if __name__=="__main__":
    print(ScreenPicTwo())