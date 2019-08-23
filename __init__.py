#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import pandas as pd
import logging


# In[2]:


# Setting information
userName = 'hiromichi@nttiur.onmicrosoft.com'
password = 'Ax2019@feb'
url = 'https://port.crm7.dynamics.com/G/Solutions/ManageSolutions.aspx?OrganizationId=401d5e0f-262c-4e16-88d8-fb454c1bd941'
browser = webdriver.Chrome('chromedriver.exe')
result = ''


# In[3]:


# Login to Dynamics admin center
def login_function():
    browser.get(url)
    sleep(5)
    Login_ID = browser.find_element_by_id('i0116')
    Login_ID.send_keys(userName)
    Login_GoNext = browser.find_element_by_id('idSIButton9')
    Login_GoNext.click()
    sleep(5)
    Login_Password = browser.find_element_by_id('i0118')
    Login_Password.send_keys(password)
    sleep(3)
    Login_GoSignIn = browser.find_element_by_id('idSIButton9')
    Login_GoSignIn.click()
    sleep(3)
    Login_KeepID_Y_or_N = browser.find_element_by_id('idSIButton9')
    Login_KeepID_Y_or_N.click()


# In[4]:


# Find solution states in each page
solutionNames = []
versions = []
validateDates = []
updateStates = []

def scraping_page():
    lists = len(browser.find_elements_by_class_name('listrow'))
    for rowNum in range(lists):
        try:
            text = browser.find_element_by_id('listgridgridrow' + str(rowNum) +'cell0').text
            global solutionNames
            solutionNames.append(text)
        except finish_scraping_this_page:
            break

    for rowNum in range(lists):
        try:
            text = browser.find_element_by_id('listgridgridrow' + str(rowNum) +'cell1').text
            global versions
            versions.append(text)
        except finish_scraping_this_page:
            break

    for rowNum in range(lists):
        try:
            text = browser.find_element_by_id('listgridgridrow' + str(rowNum) +'cell2').text
            global validateDates
            validateDates.append(text)
        except finish_scraping_this_page:
            break

    for rowNum in range(lists):
        try:
            text = browser.find_element_by_id('listgridgridrow' + str(rowNum) +'cell3').text
            global updateStates
            updateStates.append(text)
        except finish_scraping_this_page:
            break


# In[ ]:





# In[6]:


def return_result():
    logging.info('Returning result...')
    df = pd.DataFrame()
    df['Solution Name'] = solutionNames
    df['Version'] = versions
    df['Validate date'] = validateDates
    df['States'] = updateStates
    global result
    result = df.to_json(orient='records', force_ascii=False)
    logging.info('finished returning result.')


# In[7]:


def scraping_all_pages():
    nextBtn = browser.find_element_by_id('listgridNextPageButton')
    for page in range(10):
        if nextBtn.get_attribute('disabled') is not 'true':
            scraping_page()
            nextBtn.click()        
        else:
            break


# In[8]:


login_function()


# In[9]:


scraping_all_pages()


# In[10]:


return_result()
