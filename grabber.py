import webbrowser, requests, bs4, re
from selenium import webdriver
from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# url = "https://www.steamidfinder.com/lookup/kaushikr/"
# driver.get(url)
# xpath='//*[@id="profile-info"]/tbody/tr[3]/td/code'
# element = driver.find_element(By.XPATH, xpath)
# element_text = element.text
# print("Element Text:", element_text)

def start(option, key):
    if option == '64bit':
        try:
            driver = webdriver.Chrome()
            driver.get('https://www.steamidfinder.com/lookup/' + key + '/')
            username = driver.find_element(By.XPATH, '//*[@id="profile-info"]/tbody/tr[9]/td/code')
            id = driver.find_element(By.XPATH, '//*[@id="profile-info"]/tbody/tr[3]/td/code')
            print('64-Bit ID Found')
            print(username.text, id.text)
            obtain(username.text, id.text)
        except:
            print('It appears that this 64-BIT ID does not connect to registered Steam Account.')
    elif option == 'Steam':
        try:
            driver = webdriver.Chrome()
            driver.get('https://www.steamidfinder.com/lookup/'+key+'/')
            username = driver.find_element(By.XPATH, '//*[@id="profile-info"]/tbody/tr[9]/td/code')
            id = driver.find_element(By.XPATH, '//*[@id="profile-info"]/tbody/tr[3]/td/code')
            print('Steam ID Found')
            print(username.text, id.text)
            obtain(username.text, id.text)

        except:
            print('Unable to Grab SteamID. This may be because either the profile does not exist, or the given Steam ID provided is invalid.')

    else:
        print('Error')

def obtain(username, id):
    try:
        driver = webdriver.Chrome()
        driver.get('https://www.dotabuff.com/players/' + id + '/matches/')
        mainrole = driver.find_element(By.XPATH, '//*[@id="match-aggregate-stats-target"]/div[2]/div[1]')
        # secondrole = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[1]/section[1]/article/div/div[1]/div[2]/div[1]')
        # print(secondrole.text)
        print(username+' is '+mainrole.text)
    except:
        print('It appears that '+username+'\'s DOTABUFF profile is private!')
