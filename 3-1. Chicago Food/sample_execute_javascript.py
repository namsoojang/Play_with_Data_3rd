from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://en.wikipedia.org")

browser.execute_script("alert('Hello, World!')")


