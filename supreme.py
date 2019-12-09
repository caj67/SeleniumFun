from selenium import webdriver
from driver_file_path import file_path as fp
from info import *
from selenium.webdriver.support.ui import Select
from selenium import *

driver = webdriver.Chrome(fp)


driver.get("https://SupremeNewYork.com/shop/all")
driver.find_element_by_xpath("/html/body/div/ul/li[1]/div/a/img").click()
driver.implicitly_wait(1)
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/form/fieldset[2]/input").click()
driver.find_element_by_xpath("/html/body/div/div/div[1]/div/a[2]").click()
#name
driver.find_element_by_xpath(("/html/body/div[1]/div[1]/form/div[2]/div[1]/fieldset/div[1]/input")).send_keys(name)
#email
driver.find_element_by_xpath(("/html/body/div[1]/div[1]/form/div[2]/div[1]/fieldset/div[2]/input")).send_keys(email)
#phone
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/div[2]/div[1]/fieldset/div[3]/input").send_keys(phone)
#address
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/div[2]/div[1]/fieldset/div[4]/div[1]/input").send_keys(address)
#zip
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/div[2]/div[1]/fieldset/div[5]/div[1]/input").send_keys(zip)
# card number
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/div[2]/div[2]/fieldset/div[1]/div[2]/input").send_keys(card)
#cvv code
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/div[2]/div[2]/fieldset/div[1]/div[3]/div[2]/input").send_keys(cvv)
# month
select = Select(driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/div[2]/div[2]/fieldset/div[1]/div[3]/div[1]/select[1]"))
select.select_by_index(month)
#year
select2 = Select(driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/div[2]/div[2]/fieldset/div[1]/div[3]/div[1]/select[2]"))
select2.select_by_index(year)
#agree button
driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/div[2]/div[2]/fieldset/p[2]/label/div/ins").click()

# opening a broswer and maximizing it in selenium takes approximately 10 years
# we need to get a workaround
# going to be copied from stack overflow
# https://stackoverflow.com/questions/8344776/can-selenium-interact-with-an-existing-browser-session
# could also just open the browser early