# selenium has many components to use but for web browser automation we use webdriver only so, we need to import the webdriver module from selenium library.
from selenium import webdriver
import time

#The driver objects is crearted for chromebrowser using Chrome class in webdriver module.
driver = webdriver.Chrome(r"C:\Users\hp\OneDrive\Desktop\chromedriver")
#maximize_window() will maximize the browser window
driver.maximize_window()

#sleep function take seconds(int) as agrumnets and pause the excecution of the python programme.
time.sleep(5)
#minimize_window() will minimize the browser window
# driver.minimize_window()
#get function takes the website url or file as argumnet as string
#driver.get("file:file absloute path") please donot uncomment this line this is example.
driver.get("https://www.google.com/")

# please donot uncomment this line this is example.
# This is the html element of google.com search input
# <input class="gLFyf gsfi" jsaction="paste:puy29d;" maxlength="2048" name="q" type="text" aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" role="combobox" spellcheck="false" title="Search" value="" aria-label="Search" data-ved="0ahUKEwivuczgkdjzAhVhkIsKHa8yDvcQ39UDCAQ">
#find_element_by_name() function takes one agrument the value of name attribute of html element as string.
#send_keys() takes two argumnets one mandidate word to be entered in the input box and other is optional which we will discuss in later classes.
driver.find_element_by_name('q').send_keys('india')

# please donot uncomment this line this is example.
# This is the html element of google.com google search button
# < input class ="gNO89b" value="Google Search" aria-label="Google Search" name="btnK" type="submit" data-ved="0ahUKEwivuczgkdjzAhVhkIsKHa8yDvcQ4dUDCAs" >
time.sleep(5)
#find_element_by_class_name() takes one mandiate argument value of class atrribute of html element as string
# and return the html element if found else NoSuchElementException will be raised.

#click() function will not take any arguments, it perform the click action over that html element
driver.find_element_by_class_name('gNO89b').click()
time.sleep(5)
# back() function will not take any arguments, it perform back page navigation in browser.
driver.back()
time.sleep(3)
#forward() function will not take any arguments, it perform forward page navigation in browser.
driver.forward()
time.sleep(3)
# refresh() function will not take any arguments, it perform back page refresh in browser.
driver.refresh()
time.sleep(5)
#close() function will not take any arguments, it will close the tab which is in focus.
driver.close()
# quit() function will not take any arguments, it will close the entire browser even it has tab.
driver.quit()