from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os
print(os.getcwd())

browser = webdriver.Firefox()
search = 'minotaur'
# this approach didn't work as well: clicking each result and inspecting
# the result.  Only the first search result yields the URL of the actual gif in the
# src attribute.  The others give an inline encoding of the thumbnail.
# titleClass = '.Beeb4e'
secondary = '.WGvvNb'
# browser.get('https://mtaur.com/')
browser.get('https://www.google.com/search?q=' + search + '&tbm=isch&tbs=itp:animated')

searchlist = []
# links = browser.find_elements_by_css_selector('a[role="link"] img')
resultsWanted = 10

from urllib import request

for i in range(resultsWanted):
    # approach that didn't work as well
    # browser.find_elements_by_css_selector('.rg_i')[i].click()
    # time.sleep(3)
    # try:
    # titleDiv = browser.find_element_by_css_selector(titleClass)
    # searchlist.append(search + ' ' + titleDiv.text)
    # print('added ' + search + ' ' + titleDiv.text)
    #
    #
    # For some reason, only the first result is easily scraped with CSS selectors.
    # To get other results, we use the text fields of the other results to create
    # new searches targeted at fetching each result separately.
    # This approach *usually* works...
    div2 = browser.find_elements_by_css_selector(secondary)[i]
    newstr = ''.join((filter(lambda x: x not in ['#', '.', '%', '&', '?'], div2.text)))
    searchlist.append(search + ' ' + newstr)
    # except:
        # pass

j = 0
for searchTerm in searchlist:
    print(str(j))
    try:
        browser.get('https://www.google.com/search?q=' + searchTerm + '&tbm=isch&tbs=itp:animated')
        browser.find_element_by_css_selector('.rg_i').click()
        # images usually change from thumbnail inline to actual animated gif after loading a few seconds
        time.sleep(3)
        link = browser.find_element_by_css_selector('a[role="link"] img')
        print(searchTerm + ':')
        print(link.get_attribute('src'))
        request.urlretrieve(link.get_attribute('src'), 'gifs/' + search + str(j) + '.gif')
    except:
        print('Something went wrong...')
        pass
    j = j + 1
