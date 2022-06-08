import libraries
from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# from selenium import webdriver
# from selenium.webdriver import ActionChains

# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait

if __name__ == "__main__":
    # driver = wd.Chrome("/home/adam/Documents/github_mao/crawlling_mao/danawa/seleniumDriver/linux/chrome/102/chromedriver")
    # driver = wd.Chrome(service=Service(ChromeDriverManager().install()))
    
    chromedriver_autoinstaller.install()
    driver = wd.Chrome(options=Options().add_argument('headless'))
    driver.implicitly_wait(3)
    driver.get('https://www.danawa.com/')