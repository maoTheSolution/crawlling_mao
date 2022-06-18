import libraries
from bs4 import BeautifulSoup
from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

def readWebpage():
    '''
    open the url with Chrome and read the page source without a browser open
    '''
    global option, driver
    url = 'https://www.danawa.com/'
    chromedriver_autoinstaller.install()        # install chromdriver_autoinstaller
    option = wd.ChromeOptions()                 # open a webpage without a broswer open
    option.add_argument('headless')
    driver = wd.Chrome(options=option)
    driver.get(url)                             # request to open the danawa webpage
    driver.implicitly_wait(3)                   # wait 3 seconds to load the page

def htmlParseUsingSoup():
    '''
    parse the page_source with beautifulsoup4
    '''
    global option, driver, bfSoup
    html = driver.page_source 
    bfSoup = BeautifulSoup(html, 'html.parser') 

def searchCPU():
    '''
    collect cpu data   
    '''
    global bfSoup


def run():
    readWebpage()
    htmlParseUsingSoup()


if __name__ == "__main__":
    run()