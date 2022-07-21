from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.thesparksfoundationsingapore.org/")
time.sleep(10)

# Tests in the HOME page https://www.thesparksfoundationsingapore.org/ 
# 1.navigation bar is present or not
# 2.logo is present or not
# 3.does the link in footer of the page W3layouts is correct

navpres = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/nav")
if(navpres != None):
	print("yes, The navigationbar is present...")
else:
	print("no, The navigationbar is not present...")

logpres=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/h1/a/img")
if(logpres):
	print("yes, The logo for the page is present...")
else:
	print("no, The logo for the page is not present...")

flink=driver.find_element(By.XPATH,"/html/body/div[7]/p/a")
fwork=flink.get_attribute("href")
if(fwork=="http://w3layouts.com/"):
	print("yes, The link is directing to http://w3layouts.com/")
else:
	print("no, The link is not directing to http://w3layouts.com/")


time.sleep(5)
# Tests in the LINKS page https://www.thesparksfoundationsingapore.org/links/software-and-app/
# 4.checking the name (inner title ) of the page is correct
# 5.checking whether it has top hover icon or not

driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[4]/a").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[4]/ul/li[1]/a").click()
time.sleep(2)
namecheck = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/h2").text
if(namecheck=="LINKS Suite"):
	print("yes, The name in the Links page is correct")
else:
	print("no, The name in the Links page is not correct")
 	
isTopHover = driver.find_element(By.ID,"toTopHover")
if(isTopHover):
	print("yes, The top hover icon is present")
else:
	print("no, The top hover icon is not present")

#program page
# 6.copy right exist or not
# 7.checking the student mentorship program option is clicking or not

driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[3]/a").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[3]/ul/li[5]/a").click()
time.sleep(2)
copyright = driver.find_element(By.XPATH,"/html/body/div[4]")
if(copyright):
	print("yes, The copyright is present ")
else:
	print("no, The copyright is not present")

clickable = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/ul/li[2]/a")
check = clickable.get_attribute("href");
if check is not None:
	print("yes, The Student Mentorship Program option is clicking...")
else:
	print("no, The Student Mentorship Program option is not clicking...")

# contact us page
# 8.mobile icon is present on contact option or not
# 9.the map icon is present on Address option or not
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[6]/a").click()
time.sleep(5)
icon = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div[1]/i")
if(icon):
	print("The mobile icon is present on Contact option")
else:
	print("The mobile icon is not present on Contact option")


icon = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[1]/i")
if(icon):
	print("The map icon is present on Address option")
else:
	print("The map icon is not present on Address option")
# join us page
# 10.the submit button is present or not

driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[5]/a").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/nav/div[2]/nav/ul/li[5]/ul/li[1]/a").click()
time.sleep(2)

submit=driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div/form/input[3]")
if(submit):
	print("yes, The submit option is present")
else:
	print("no, The submit option is not present")
time.sleep(10)
driver.close()
