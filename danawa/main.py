import libraries
from bs4 import BeautifulSoup
from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

def readWebpage(url):
    '''
    open the url with Chrome and read the page source without a browser open
    '''
    global option, driver
    chromedriver_autoinstaller.install()        # install chromdriver_autoinstaller
    option = wd.ChromeOptions()                 # open a webpage without a broswer open
    # option.add_argument('headless')
    # driver = wd.Chrome(options=option)
    driver = wd.Chrome()
    driver.get(url)                             # request to open the danawa webpage
    driver.implicitly_wait(5)                   # wait 30 seconds to load the page. If it ends early, move on and save time.

    element = driver.find_element(by=By.XPATH, value='//*[@id="danawa_menubar"]/div[2]/a[3]') # open a component page 
    element.click()
    parent = driver.window_handles[0]            # set the current driver as parent
    child = driver.window_handles[1]             # set the new tab a s a child
    driver.switch_to.window(child)               # move to the child 

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
    global driver, cpu
    cpu = dict()
    for each in range(1, 32):
        title = driver.find_element(by=By.XPATH, value='//*[@id="estimateMainProduct"]/div/div[2]/div[2]/table/tbody/tr['+ str(each) + ']/td[2]/p/a')
        price = driver.find_element(by=By.XPATH, value='//*[@id="estimateMainProduct"]/div/div[2]/div[2]/table/tbody/tr['+ str(each) +']/td[3]/p/span')
        cpu[title.text] = price.text

    for each in cpu.items():
        print(each)

    # print('PageContents:{}'.format(driver.page_source))


    # WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="categoryUnit97"]/ul/li[1]/a'))).click()
    # html = driver.page_source 
    # bfSoup = BeautifulSoup(html, 'html.parser')

    # print(bfSoup.prettify())



def run():
    readWebpage('https://www.danawa.com/')
    # htmlParseUsingSoup()
    searchCPU()


if __name__ == "__main__":
    run()