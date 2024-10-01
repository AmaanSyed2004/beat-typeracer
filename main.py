from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import keyboard
import pyautogui

def get_text(driver):
    time.sleep(1) #wait for page to load
    src=driver.page_source
    soup=BeautifulSoup(src,'html.parser')
    #logic: the text is in a span tag with property unselectable
    #find all span tags and check if unselectable is in the tag
    span= soup.find_all('span')
    #now, each character is in a span tag, so we need to concatenate all the text in the span tags with unselectable property
    text = ''
    for i in span:
        if "unselectable" in str(i):
            text+=i.text
    if not text:
        print('No text found')
        return None
    print(text)
    return text
    
if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True) #to keep the browser open after the script ends

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://play.typeracer.com/')

    keyboard.wait('ctrl+alt')
    text=get_text(driver)
    #interval: reduce it to increase the typing speed
    #tip: going 0.02 or below will make the typing speed too fast for the website to handle
    if text:
        pyautogui.typewrite(text, interval=0.1)