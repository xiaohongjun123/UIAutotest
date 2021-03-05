from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--mute-audio")
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)

options.add_argument("--headless")
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path="/opt/google/chrome/chromedriver", options=options)

driver.get("https://www.baidu.com")
print(driver.title)
driver.quit()
