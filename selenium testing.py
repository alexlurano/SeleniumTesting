# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Chrome()

# point at current environment - change this for Dev / Prod
driver.get("localhost")

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

# generate a alert via javascript
# driver.execute_async_script(script)

print(driver.get_screenshot_as_file("foo.png"))