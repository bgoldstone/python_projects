# tried to develop linkedin email scraper and failed
from selenium import webdriver
import requests
import csv

contacts = []
driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://linkedin.com/')
driver.find_element_by_id('session_key').send_keys(input("email"))
driver.find_element_by_id('session_password').send_keys(input("password"))
driver.find_element_by_class_name('sign-in-form__submit-button').click()
driver.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')
for i in driver.find_elements_by_class_name('mn-connection-card artdeco-list ember-view'):
    driver.get("https://linkedin.com" + driver.find_element_by_class_name(
        'mn-connection-card__picture ember-view').get_attribute('href'))
    name = driver.find_element_by_class_name('artdeco-entity-lockup__title ember-view')
    driver.get(driver.current_url + 'detail/contact=info')
    email = driver.find_element_by_class_name('pv-contact-info__contact-link link-without-visited-state t-14').get_attribute('href')
    print(name + " " + email)
# def csv_writer(data):
#     with open('contacts.csv') as csv_file:
#         writer = csv.writer(csv_file, delimiter=',')
#         for line in data:
#             writer.writerow(line)
