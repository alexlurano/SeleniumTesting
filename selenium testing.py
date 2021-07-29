# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Chrome()

# point at current environment - change this for Dev / Prod
driver.get("localhost")
# set the timeout for page loading at 30 seconds
driver.set_page_load_timeout(30)

# custom login for bot - change this to match login info
user_name_input = driver.find_element_by_name("Username")
user_name_input.clear()

user_name_input.send_keys("botusername")
user_name_input = driver.find_element_by_name("Username")
user_name_input.clear()

#navigate to claim
driver.get("localhost/yadayada(claimid)")
patient_name = driver.find_element_by_name("patient name")
if (patient_name != currentclaim.name)
    print("claim currentclaim.id name mismatch please verify")
    #proceed to next claim in list

# if the name matches the expected name, proceed to stay screen
stay_link = driver.find_element_by_name("Stay") # todo -check metadata to find actual name of this element

action = ActionChains(driver)

action.click(on_element = stay_link)

action.preform()
driver.implicitly_wait(30)

#once stay screen fully loads create CAR log based on closure type.
create_stay_log = driver.find_element_by_name("Stay Log")
create_stay_log.click()
wait = WebDriverWait(driver, 30)
create_stay_log = wait.until(EC.presence_of_element_located("check metadata of pop up for unique elements") #TODO
staylog_type = driver.find_element_by_name("log type")
staylog_type.select_by_visible_text("CAR")
staylog_message = driver.find_element_by_name("title")
staylog_message.send_keys("CANNED CLOSE MESSAGE")
staylog_submit = driver.find_element_by_name("Submit")
staylog_submit.click()
driver.implicitly_wait(30)


#close claim using closure reason
claim_close = driver.find_element_by_name("close claim")
claim_close.click()

#todo - popup menu click for yes/no

close_reason = driver.find_element_by_name("close reason")
close_reason.select_by_visible_text("close reason goes here")
# TODO handling for the second drop down of claim closure
# TODO write a note for close note
# TODO navigate back to claim screen and confirm claim has been closed
