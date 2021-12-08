# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# create webdriver object

def find_top_tweet():
    driver.get("https://trends24.in/united-states/")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/ol")))
    best_tweet = driver.find_element_by_xpath(("//div[@class='trend-card']"))
    top_tweet_now = best_tweet.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[1]/ol/li[1]/a")
    print("ta da" + top_tweet_now.text)
    return top_tweet_now.text

def make_a_meme():
    driver.get("https://imgflip.com/memegenerator/27596988/Free")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "mm-select-popular")))
    popular_stuff = driver.find_element_by_id("mm-select-popular")
    for dank in popular_stuff.find_elements_by_class_name('im'):
        print(dank.get_attribute('title'))
    return

def find_that_link():
    driver.get("https://www.google.com/search?q=arf&rlz=1C1CHBF_enUS862US862&oq=arf&aqs=chrome..69i57j0i433i512j0i512j0i10i512j0i433i512l3j0i512j0i433i512l2.1453j0j9&sourceid=chrome&ie=UTF-8")
    #WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/ol")))
    time.sleep(3)
    best_tweet = driver.find_element_by_tag_name('h3')
    best_tweet.click()
    print("ta da" + top_tweet_now.text)
    return top_tweet_now.text

#----------------------------------
#----------------------------------
#----------------------------------
#----------------------------------
driver = webdriver.Chrome()
#tweet_txt = find_top_tweet()
#make_a_meme()

find_that_link() 
driver.close()





