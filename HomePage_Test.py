# Import Selenium Webdriver
from selenium import webdriver

# Define Global Variables
global driver
driver = webdriver.Chrome()

# Use Chrome driver
def test_setup():
    # Open Cushman UAT URL
    driver.get('https://qa-sitecore-www.cushmanwakefield.com/en')
    driver.implicitly_wait(10)
    driver.maximize_window()

#def test_logoImage():
 #   logoImage =driver.find_element_by_css_selector('body > header > div.container.clearfix > a > button > img').is_displayed()
  #  print(logoImage)
   # print("Hello Logo loaded successfully")


def test_popupHandler():
    # Click on Privacy Agreement
    Privacy_Agree = driver.find_element_by_xpath('//*[@id="c-p-bn"]')
    Privacy_Agree.click()

    # close Popup window
    letMeContinue_Button = driver.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/button')
    letMeContinue_Button.click()


def test_changeCountry():
    country_icon = driver.find_element_by_xpath('/html/body/header/div[1]/ul[2]/li[1]/button/span')
    country_icon.click()


def test_selectCountry():
    country_SearchText = driver.find_element_by_xpath('//*[@id="searchString"]')
    country_SearchText.send_keys("Canada")
    country_SelectItem = driver.find_element_by_xpath('/html/body/header/div[1]/ul[2]/li[1]/div/ul/li[7]/a/span[2]')
    country_SelectItem.click()
    driver.implicitly_wait(15)

#def test_openNavigationMenu():
 #   openNavigationMenu = driver.find_element_by_xpath('/html/body/header/div[1]/button/i[1]/span')
  #  openNavigationMenu.click()

def test_peoplePage():

    people_link = driver.find_element_by_css_selector('body > header > div.container.clearfix > ul.header-nav > li:nth-child(1) > a')
    people_link.click()


def test_propertiesPage():
    properties_link = driver.find_element_by_css_selector('body > header > div.container.clearfix > ul.header-nav > li:nth-child(2) > a')
    properties_link.click()


def test_insightsPage():
    insights_link = driver.find_element_by_css_selector('body > header > div.container.clearfix > ul.header-nav > li:nth-child(3) > a')
    insights_link.click()


def test_servicesPage():
    services_link = driver.find_element_by_css_selector('body > header > div.container.clearfix > ul.header-nav > li:nth-child(4) > a')
    services_link.click()



# logoImage.location = 'https://qa-sitecore-www.cushmanwakefield.com:443/-/media/cw/global/about-us/logo.svg'
##Search_Button=driver.find_element_by_xpath(/html/body)
# Search_Button.click()

# Close all the browsers
# def test_teardown():
#    driver.quit()
