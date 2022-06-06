import os
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

'''
다나와 싸이트에서 제품과 그 가격을 가져와 txt파일로 저장하는 프로그램을 만든다
저장 장소는 사용자 정의로 한다
필요한 환경설치를 위하여 beautifulsout4, selenium 우선 설치
'''



def listPip():
    '''
    return a list of all pip libraries are being installed
    '''
    output  = os.popen('pip3 list').readlines()
    newStr_list = []
    for each in range(2,len(output)):
        newStr = ''
        for s in output[each]:
            if(s == ' '):
                break
            newStr = newStr + s
        newStr_list.append(newStr)

    return newStr_list

def installLibrary(*name):
    '''
    update pip first and install the required libraries
    '''
    os.system('pip3 install --upgrade pip')
    target = 'pip3 install '
    for each in name:
        os.system(target+each[0])

def filterLibraries():
    '''
    return a list of libraires that need to be installed
    '''
    allLibraries = listPip()
    targetLibraries = []
    if('selenium' not in allLibraries):
        targetLibraries.append('selenium')
    if('beautifulsoup4' not in allLibraries):
        targetLibraries.append('beautifulsoup4')

    return targetLibraries

def run():
    '''
    run the functions in order
    '''

    if(len(filterLibraries()) == 0):
        print("all satisfied")
    else:
        installLibrary(filterLibraries())
        print("now all installed")

if __name__ == "__main__":
    run()
