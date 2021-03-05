from selenium import webdriver
import os
from PIL import Image
import time
def ScreenPic():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\testreport\\UIAutoTestReport.html")
    filename = "Screemshot.png"
    time.sleep(2)
    driver.save_screenshot(filename)
    ele = driver.find_element_by_xpath('''/html/body/div[2]/div[1]/div''')
    left = ele.location["x"]
    top = ele.location["y"]
    print(ele.location)
    right = left + ele.size["width"]
    bottom = top + ele.size["height"]
    print(ele.size)
    im = Image.open(filename)
    im1 = im.crop((left, top, right, bottom))
    im1.save(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\testreport\\"+filename)


if __name__=="__main__":
    ScreenPic()