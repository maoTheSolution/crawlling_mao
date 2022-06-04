import os
os.system('pip3 install --upgrade pip')
os.system('pip3 install selenium')
os.system('pip3 install beautifulsoup4')

'''
다나와 싸이트에서 제품과 그 가격을 가져와 txt파일로 저장하는 프로그램을 만든다
저장 장소는 사용자 정의로 한다
필요한 환경설치를 위하여 beautifulsout4, selenium 우선 설치
'''



import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

