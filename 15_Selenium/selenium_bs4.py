from selenium import webdriver
from bs4 import BeautifulSoup
import codecs

driver = webdriver.Chrome("C:/Users/multicampus/Downloads/chromedriver.exe")
driver.get("https://namu.wiki/w/%EC%A0%9C20%EB%8C%80%20%EA%B5%AD%ED%9A%8C%EC%9D%98%EC%9B%90")
print(driver.find_element_by_xpath("/html/body/div/div/div[2]/article/div[3]/div[2]/div/div/h3[1]").text)