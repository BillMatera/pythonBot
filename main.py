## imports:

## selenium for web driving
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
## time for pausing between navigation
import time

## Datetime for recording time of submission
import datetime


## functions:

## init funtion 
def in_it():
  print("in_it method ")
  ##amazon_auth() 
  headless_test()

def headless_test():
  options = Options()
  options.headless = True
  driver = webdriver.Chrome(chrome_options=options)  
  driver.get("https://www.google.com/search?q=dogs")


  # capture the screen
  driver.get_screenshot_as_file("capture.png")

## sign user into amazon
def amazon_auth():
  print("amazon_auth method")
  ## using Chrome to access web
  chromeBrowser = webdriver.Chrome()

  ## open amazon home
  chromeBrowser.get('https://amazon.com')

  ## hover sign in element to display sign in button
  hover_el = chromeBrowser.find_element_by_id('nav-link-accountList')
  Hover = ActionChains(chromeBrowser).move_to_element(hover_el)
  Hover.perform()

  ## click signIn button to redirect to sign in page
  hover_el.click()

  ## on sign in page 
  ## find input field elements
  email_field = chromeBrowser.find_element_by_id('ap_email')
  password_field = chromeBrowser.find_element_by_id('ap_password')

  ## fill in fields with acct credentials 
  email_field.send_keys('matera@optonline.net')
  password_field.send_keys('Amazon4me')
  
  ## trigger signin action
  chromeBrowser.find_element_by_id('signInSubmit').click()

  time.sleep(5)

  chromeBrowser.quit()
  print("amazon_auth end")


## main function
if __name__ == "__main__":
  print("__main__ method ")
  ## call init to start flow
  in_it()

