from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def web_hhandler(timetable,username,number):

    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Ensure GUI is off
    webdriver_path = '/home/shimroo/Internships/summer 23/proj/course/chromedriver'
    chrome_options.add_experimental_option("prefs", {
    "download.default_directory": "/home/shimroo/Internships/summer 23/proj/course/schedule",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
    })
    service = Service(webdriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://gizmoa.com/college-schedule-maker/")
    time.sleep(2)  # Adjust the delay if necessary

    #buttons
    add_item = driver.find_element(by= By.XPATH,value='//*[contains(concat( " ", @class, " " ), concat( " ", "addButton", " " ))]')
    # course_code = driver.find_element( by= By.CSS_SELECTOR, value='input[placeholder=''required'']')
    name = "input[placeholder='Schedule Title']"
    mon = 'body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)'
    tue = 'body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > input:nth-child(1)'
    wed = 'body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > input:nth-child(1)'
    thu = 'body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > input:nth-child(1)'
    fri = 'body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > div:nth-child(1) > div:nth-child(5) > div:nth-child(2) > input:nth-child(1)'
    sat = 'body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > div:nth-child(1) > div:nth-child(7) > div:nth-child(2) > input:nth-child(1)'
    sun = 'body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > table:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > div:nth-child(1) > div:nth-child(8) > div:nth-child(2) > input:nth-child(1)'
    start_hr = 'body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > table:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)'
    start_min = 'body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > table:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > input:nth-child(3)'
    end_hr = 'body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > table:nth-child(2) > tr:nth-child(2) > td:nth-child(2) > input:nth-child(1)'
    end_min = 'body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > table:nth-child(2) > tr:nth-child(2) > td:nth-child(2) > input:nth-child(3)'
    section = "//input[@placeholder='optional (ex. Lab)']"
    instructor = 'body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(3) > table:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > input:nth-child(1)'
    done = '.fhy1ww9'
    screenshot = "//label[normalize-space()='Save Image']"
    setting = "//div[@class='flx7rbn']//*[name()='svg']"
    hour_24 = "//div[normalize-space()='24 Hour']"

    driver.find_element( by= By.XPATH, value=setting).click()
    time.sleep(0.5)  # Adjust the delay if necessary
    driver.find_element( by= By.XPATH, value=hour_24).click()
    

    driver.find_element( by= By.CSS_SELECTOR, value=name).send_keys(username+" "+str(number))

    for course in timetable:
        #process
        add_item.click()    #adds a new course
        time.sleep(0.5)  # Adjust the delay if necessary
        active_element = driver.switch_to.active_element
        active_element.send_keys(course.code)   #enters the coourse.code
        # time.sleep(0.5)  # Adjust the delay if necessary

        #selecting days
        if 'M' in course.days:
            item = driver.find_element( by= By.CSS_SELECTOR, value=mon)
            item.click()
        if 'T' in course.days:
            item = driver.find_element( by= By.CSS_SELECTOR, value=tue)
            item.click()
        if 'W' in course.days:
            item = driver.find_element( by= By.CSS_SELECTOR, value=wed)
            item.click()
        if 'R' in course.days:
            item = driver.find_element( by= By.CSS_SELECTOR, value=thu)
            item.click()
        if 'F' in course.days:
            item = driver.find_element( by= By.CSS_SELECTOR, value=fri)
            item.click()
        if 'S' in course.days:
            item = driver.find_element( by= By.CSS_SELECTOR, value=sat)
            item.click()
        if 'U' in course.days:
            item = driver.find_element( by= By.CSS_SELECTOR, value=sun)
            item.click()


        driver.find_element( by= By.CSS_SELECTOR, value=start_hr).send_keys(course.SH) 
        # print("dfa",course.SM)
        sm = driver.find_element( by= By.CSS_SELECTOR, value=start_min)
        sm.click()
        sm.send_keys(course.SM)    
        driver.find_element( by= By.CSS_SELECTOR, value=end_hr).send_keys(course.EH)    
        # print("fdaf",course.EM)
        em = driver.find_element( by= By.CSS_SELECTOR, value=end_min)
        em.click()    
        em.send_keys(course.EM)
        # time.sleep(10)  # Adjust the delay if necessary
        
        driver.find_element( by= By.XPATH, value=section).send_keys(course.section)
        driver.find_element( by= By.CSS_SELECTOR, value=instructor).send_keys(course.instructor) 

        # time.sleep(.5)  # Adjust the delay if necessary

        driver.find_element( by= By.CSS_SELECTOR, value=done).click() 
    
    # time.sleep(1)
    # driver.save_screenshot("timetable_screenshot.png")

    driver.find_element( by= By.XPATH, value=screenshot).click() 
    print("timetable:",username+" "+str(number),"saved")
    time.sleep(1)


    # Take a screenshot of the timetable

    # Close the browser
    driver.quit()
