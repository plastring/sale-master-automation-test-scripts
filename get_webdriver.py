# coding = utf-8

from selenium import webdriver

def get_webdriver_of_Chrome():
    browser = webdriver.Chrome(r"C:\Users\rehai\Downloads\chromedriver_win32\chromedriver.exe")
    return browser