from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys,ActionChains
import time
import datetime

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('D:\Code\Selenium\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()


login = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
password= 'secret_sauce'

#AUTHORISATION NEGATIVE
user_name = driver.find_element(By.XPATH,'//input[@id="user-name"]')
user_name.send_keys(login[0])
user_name.send_keys(Keys.BACKSPACE)
user_name.send_keys(Keys.BACKSPACE)
user_name.send_keys(Keys.BACKSPACE)
user_name.send_keys(Keys.BACKSPACE)
print('input login')

user_password = driver.find_element(By.XPATH,'//input[@id="password"]')
user_password.send_keys(password)
time.sleep(1)
user_password.send_keys(Keys.RETURN)
print('input password')
n=1
name='screen'+str(n)+'.png'
driver.save_screenshot(name)
n+=1
driver.refresh()

#AUTHORISATION POSITIVE

user_name = driver.find_element(By.XPATH,'//input[@id="user-name"]')
user_name.send_keys(login[0])
print('input login')

user_password = driver.find_element(By.XPATH,'//input[@id="password"]')
user_password.send_keys(password)
user_password.send_keys(Keys.RETURN)
print('input password')

#SORT PRODUCTS

filter = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div[2]/span/select' )
filter.click()
filter.send_keys(Keys.DOWN)
filter.send_keys(Keys.DOWN)
time.sleep(2)
filter.send_keys(Keys.RETURN)

name='screen'+str(n)+'.png'
driver.save_screenshot(name)
n+=1

#INFO_PRODUCT_1
product_1=driver.find_element(By.XPATH,'//a[@id="item_4_title_link"]')
value_product_1 = product_1.text
print(value_product_1)
price_product_1 = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div/div/div[5]/div[2]/div[2]/div')
value_price_1=price_product_1.text
print(value_price_1)

add_to_cart_button1 = driver.find_element(By.XPATH,'//button[@id="add-to-cart-sauce-labs-backpack"]')
add_to_cart_button1.click()
print('Add_product_1_to _cart')

#INFO_PRODUCT_2
product_2=driver.find_element(By.XPATH,'//*[@id="item_0_title_link"]/div')
value_product_2 = product_2.text
print(value_product_2)
price_product_2 = driver.find_element(By.CSS_SELECTOR,'#inventory_container > div > div:nth-child(2) > div.inventory_item_description > div.pricebar > div')
value_price_2=price_product_2.text
print(value_price_2)
add_to_cart_button2= driver.find_element(By.XPATH,'//button[@id="add-to-cart-sauce-labs-bike-light"]')
add_to_cart_button2.click()
print('Add_product_2_to _cart')



cart=driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a')
cart.click()
print('Enter_Cart')

name='screen'+str(n)+'.png'
driver.save_screenshot(name)
n+=1

#INFO_CART_PRODUCT_1

product_1_cart=driver.find_element(By.XPATH,'//a[@id="item_4_title_link"]')
value_product_1_cart = product_1_cart.text
print(value_product_1_cart)
assert value_product_1 == value_product_1_cart
print('THE NAME1 IS CORRECT"')
price_product_1_cart = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/div')
value_price_1_cart=price_product_1_cart.text
print(value_price_1_cart)
assert value_price_1 == value_price_1_cart
print ("THE PRICE1 IS CORRECT")

#INFO_CART_PRODUCT_2

product_2_cart=driver.find_element(By.XPATH,'//*[@id="item_0_title_link"]/div')
value_product_2_cart = product_2_cart.text
print(value_product_2_cart)
assert value_product_2 == value_product_2_cart
print('THE NAME2 IS CORRECT"')
price_product_2_cart = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div[1]/div[4]/div[2]/div[2]/div')
value_price_2_cart=price_product_2_cart.text
print(value_price_2_cart)
assert value_price_2 == value_price_2_cart
print ("THE PRICE2 IS CORRECT")

#CHECKOUT

checkout=driver.find_element(By.XPATH, '//button[@id="checkout"]')
checkout.click()
print("CLICK")
#SELECT USER
first_name= "Ivan"
last_name = "Petrov"
zip_code=198343

first_name_input = driver.find_element(By.XPATH,'//input[@id="first-name"]')
first_name_input.send_keys(first_name)
last_name_input = driver.find_element(By.XPATH,'//input[@id="last-name"]')
last_name_input.send_keys(last_name)
zip_code_input = driver.find_element(By.XPATH,'//input[@id="postal-code"]')
zip_code_input.send_keys(zip_code)

name='screen'+str(n)+'.png'
driver.save_screenshot(name)
n+=1
print( "FORM_FILLED")

continue_button = driver.find_element(By.XPATH,'//input[@id="continue"]')
continue_button.click()
print('ORDERED')


product_1_order=driver.find_element(By.XPATH,'//*[@id="item_4_title_link"]/div')
value_product_1_order = product_1_order.text
print(value_product_1_order)
assert value_product_1 == value_product_1_order
print('THE NAME1 IN ORDER IS CORRECT"')

product_2_order=driver.find_element(By.XPATH,'//*[@id="item_0_title_link"]/div')
value_product_2_order = product_2_order.text
print(value_product_2_order)
assert value_product_2 == value_product_2_order
print('THE NAME2 IN ORDER IS CORRECT"')

price_product_1_order= driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/div')
value_price_1_order=price_product_1_order.text
print(value_price_1_order)
assert value_price_1 == value_price_1_order
print ("THE PRICE IN ORDER IS CORRECT")

price_product_2_order= driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div[1]/div[4]/div[2]/div[2]/div')
value_price_2_order=price_product_2_order.text
print(value_price_2_order)
assert value_price_2 == value_price_2_order
print ("THE PRICE2 IN ORDER IS CORRECT")

#Summary

total_price_in_order = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div[2]/div[5]')
value_total_price_in_order=total_price_in_order.text
print (value_total_price_in_order)
price1 = float(value_price_1_order[1::])
price2 = float(value_price_2_order[1::])
print(price1)
print(price2)
sum1 = f'Item total: ${price1+price2}'
print(sum1)
#sum_order=float(value_total_price_in_order[1::])
#print(sum_order)
assert sum1 == value_total_price_in_order
print("THE SUM IS OK")

driver.execute_script("window.scrollTo(0,800)")
finish_button = driver.find_element(By.XPATH,'//button[@id="finish"]')
finish_button.click()

name='screen'+str(n)+'.png'
driver.save_screenshot(name)
n+=1
print('TEST COMPLITED')
driver.close()

##### Go back and forward#####
# driver.back()
# goes one stap back
# driver.forward()
# goes one step forward

#### Right and DoubleClick####
# action=ActionChains(driver)
# button_doublecl = driver.find_element(By.XPATH,'//button[@id="doubleClickBtn"]')
# action.double_click(button_doublecl).perform()
# time.sleep(2)
# priint('OK')
#
# action=ActionChains(driver).perform()
# button_rightcl = driver.find_element(By.XPATH,'//button[@id="rightClickBtn"]')
# action.context_click(button_rightcl)
# print('OK')