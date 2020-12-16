import getpass
from selenium import webdriver
from selenium.webdriver.common import keys
import sys, time

url = "url to site"
url_hci = "url to site"
login = input("Enter login: ")
password = getpass.getpass("Enter password: ")

options = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "/Users/Filip.Chromy/Desktop/Work/Fakturace/Download_fakturace"}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)
driver.get(url)

username = driver.find_element_by_id("username")
username.click()
username.send_keys(login)

pw = driver.find_element_by_id("password")
pw.click()
pw.send_keys(password)

submit_button = driver.find_element_by_id("submitButton")
submit_button.click()

hci = driver.get(url_hci)

fakturace_hci = driver.find_element_by_link_text("Přejít na vyúčtování")
fakturace_hci.click()
time.sleep(2)

fakturace_rijen = driver.find_element_by_link_text("Vyúčtování za říjen 2020")
fakturace_rijen.click()

fakturace_download = driver.get("url to site")