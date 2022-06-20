from email import charset
import libraries
from bs4 import BeautifulSoup
from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By

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
    rows = len(driver.find_elements(by=By.XPATH, value='//*[@id="estimateMainProduct"]/div/div[2]/div[2]/table/tbody/tr'))
    for each in range(1, rows):
        title = driver.find_element(by=By.XPATH, value='//*[@id="estimateMainProduct"]/div/div[2]/div[2]/table/tbody/tr['+ str(each) + ']/td[2]/p/a')
        price = driver.find_element(by=By.XPATH, value='//*[@id="estimateMainProduct"]/div/div[2]/div[2]/table/tbody/tr['+ str(each) +']/td[3]/p/span')
        cpu[cpuTitleFilter(title.text)] = strIntoNumber(price.text)


def displayCPU():
    '''
    dispaly all cpu info
    '''
    global cpu
    for each in cpu.items():
        print(each)

def strIntoNumber(number):
    '''
    string into number and return it
    '''
    num = ''
    for each in number:
        if(each != ","):
            num = num + each

    return int(num)

def cpuTitleFilter(name):
    '''
    get rid of the parenthsis after parts
    '''
    newName = ''
    for each in name:
        if(each == '('):
            break
        newName = newName + each
    
    return newName[0:-1]

def intelOnly():
    ''' 
    collect only intel cpus
    '''
    global intel, cpu
    intel = dict()
    for each in cpu.keys():
        if('인텔' in each):
            intel[each] = cpu[each]

def displayIntelOnly():
    '''
    display Intel cpu only
    '''
    global intel
    for each in intel.items():
        print(each)

def displayRyzen():
    '''
    display Ryzen only
    '''
    global ryzen
    for each in ryzen.items():
        print(each)

def ryzenOnly():
    '''
    collect only ryzen cpus
    '''
    global ryzen, cpu
    ryzen = dict()
    for each in cpu.keys():
        if('AMD' in each):
            ryzen[each] = cpu[each]


def findYourCPUs(company, howGood):
    '''
    return a list of the cpu titles that satisfy the needs
    howGood : i9, i7, i5 or i3
            : 라이젠7,  라이젠7 or 라이젠3    
    '''
    global intel, ryzen 
    output = []

    if(company== '인텔'):
        for each in intel.keys():
            if(howGood in each):
                output.append(each)
    else:
        for each in ryzen.keys():
            if(howGood in each):
                output.append(each)

    return output


def findTheCheapestCPU(sampleL):
    '''
    receive a list of cpu tiltes and return a cheapest one taht satisfy the requirements
    '''
    global cpu

    temp = ''
    tempPrice = 0
    for each in sampleL:
        if(temp == ''):
            temp = each
            tempPrice = cpu[each]
        else :
            if(tempPrice > cpu[each]):
                temp = each
                tempPrice = cpu[each]
    
    return temp

def readChart():
    '''
    read a chart text file and return the data as a dictionary
    '''
    global chart, programTable
    programTable = dict()
    chart = open('./chart.txt', 'r').readlines()
    for each in chart:
        eachList = each.rstrip().split(',')
        


        


def run():
    # readWebpage('https://www.danawa.com/')
    # htmlParseUsingSoup()
    # searchCPU()
    # displayCPU()
    # intelOnly()
    # ryzenOnly()
    # displayIntelOnly()
    # displayRyzen()
    # print(findYourCPUs('인텔', 'i7'))
    # print(findTheCheapestCPU(findYourCPUs('인텔', 'i7')))
    # print(findYourCPUs('AMD', '라이젠7'))
    # print(findTheCheapestCPU(findYourCPUs('AMD', '라이젠7')))
    readChart()

if __name__ == "__main__":
    run()