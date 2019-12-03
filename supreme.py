from selenium import webdriver
from driver_file_path import file_path as fp
from selenium import *

# right click on chromedriver.exe copy the path, and paste it after the r

driver = webdriver.Chrome(fp)
# here is your file path Barl
# "C:\Users\Carl\PycharmProjects\seleniumtest2\drivers\chromedriver.exe"

driver.get("https://SupremeNewYork.com/shop")
# driver.maximize_window()

# opening a broswer and maximizing it in selenium takes approximately 10 years
# we need to get a workaround
# going to be copied from stack overflow
# https://stackoverflow.com/questions/8344776/can-selenium-interact-with-an-existing-browser-session
# could also just open the browser early
