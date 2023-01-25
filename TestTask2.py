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


# HELLO
print('Приветствую тебя в нашем интернет магазине')
print('''
Выбери один из следующих товаров и укажи его номер
1 - Sauce Labs Backpack -$29.99
2 - Sauce Labs Bike Light - $9.99
3 - Sauce Labs Bolt T-Shirt - $15.99
4 - Sauce Labs Fleece Jacket - $49.99
5 - Sauce Labs Onesie - $7.99
6 - Test.allTheThings() T-Shirt (Red) - $15.99
''')
product_num=int(input())
assert 1<=product_num<=6 , "You've entered incorrect value"
print("введен корректный номер")



login = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
password= 'secret_sauce'


#AUTHORISATION POSITIVE

user_name = driver.find_element(By.XPATH,'//input[@id="user-name"]')
user_name.send_keys(login[0])
print('input login')

user_password = driver.find_element(By.XPATH,'//input[@id="password"]')
user_password.send_keys(password)
user_password.send_keys(Keys.RETURN)
print('input password')


#INFO_PRODUCTS
  #CREATING PRODUCTS
class Product():
    def __init__(self, number, name,price,add_button):
        self.number=number
        self.name=name
        self.price=price
        self.add_button=add_button
    def inform(self):
       print( f'Вы выбрали товар №{self.number}, {self.name}, стоимостью {self.price}')


product_1name=driver.find_element(By.XPATH,'//*[@id="item_4_title_link"]/div')
value_product_1 = product_1name.text
price_product_1 = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div')
value_price_1=price_product_1.text
add_to_cart_button1 = driver.find_element(By.XPATH,'//button[@id="add-to-cart-sauce-labs-backpack"]')
print(value_product_1)
print(value_price_1)


product_2name=driver.find_element(By.XPATH,'//*[@id="item_0_title_link"]/div')
value_product_2 = product_2name.text
price_product_2 = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div')
value_price_2=price_product_2.text
add_to_cart_button2 = driver.find_element(By.XPATH,'//button[@id="add-to-cart-sauce-labs-bike-light"]')
print(value_product_2)
print(value_price_2)



product_3name=driver.find_element(By.XPATH,'//*[@id="item_1_title_link"]/div')
value_product_3 = product_3name.text
price_product_3 = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div')
value_price_3=price_product_3.text
add_to_cart_button3 = driver.find_element(By.XPATH,'//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
print(value_product_3)
print(value_price_3)



product_4name=driver.find_element(By.XPATH,'//*[@id="item_5_title_link"]/div')
value_product_4 = product_4name.text
price_product_4 = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[2]/div')
value_price_4=price_product_4.text
add_to_cart_button4 = driver.find_element(By.XPATH,'//button[@id="add-to-cart-sauce-labs-fleece-jacket"]')
print(value_product_4)
print(value_price_4)


product_5name=driver.find_element(By.XPATH,'//*[@id="item_2_title_link"]/div')
value_product_5 = product_5name.text
price_product_5 = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div/div/div[5]/div[2]/div[2]/div')
value_price_5=price_product_5.text
add_to_cart_button5 = driver.find_element(By.XPATH,'//button[@id="add-to-cart-sauce-labs-fleece-jacket"]')
print(value_product_5)
print(value_price_5)


product_6name=driver.find_element(By.XPATH,'//*[@id="item_3_title_link"]/div')
value_product_6 = product_6name.text
price_product_6 = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div/div/div[6]/div[2]/div[2]/div')
value_price_6=price_product_6.text
add_to_cart_button6 = driver.find_element(By.XPATH,'//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
print(value_product_6)
print(value_price_6)



PR1= Product(1, value_product_1, value_price_1, add_to_cart_button1)
PR2= Product(2, value_product_2, value_price_2, add_to_cart_button2)
PR3= Product(3, value_product_3, value_price_3, add_to_cart_button3)
PR4= Product(4, value_product_4, value_price_4, add_to_cart_button4)
PR5= Product(5, value_product_5, value_price_5, add_to_cart_button5)
PR6= Product(6, value_product_6, value_price_6, add_to_cart_button6)


#добавление продукта в корзину
Choise={1:PR1, 2:PR2, 3:PR3, 4:PR4, 5:PR5, 6:PR6}
Product_Chosen= Choise[product_num]
print('выбран продукт')
print(Product_Chosen)
Product_Chosen.inform()
push_add_to_cart_button = Product_Chosen.add_button
push_add_to_cart_button.click()
print("Товар добавлен в корзину")


cart=driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a')
cart.click()
print('Enter_Cart')


#INFO_CART_PRODUCT_1

product_1_cart=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/a/div')
value_product_1_cart = product_1_cart.text
print(value_product_1_cart)
assert Product_Chosen.name == value_product_1_cart
print('THE NAME1 IS CORRECT"')
price_product_1_cart = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/div')
value_price_1_cart=price_product_1_cart.text
print(value_price_1_cart)
assert Product_Chosen.price == value_price_1_cart
print ("THE PRICE1 IS CORRECT")

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

print( "FORM_FILLED")

continue_button = driver.find_element(By.XPATH,'//input[@id="continue"]')
continue_button.click()
print('ORDERED')


product_1_order=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/a/div')
value_product_1_order = product_1_order.text
print(value_product_1_order)
assert Product_Chosen.name == value_product_1_order
print('THE NAME1 IN ORDER IS CORRECT"')


price_product_1_order= driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/div')
value_price_1_order=price_product_1_order.text
print(value_price_1_order)
assert Product_Chosen.price == value_price_1_order
print ("THE PRICE IN ORDER IS CORRECT")



driver.execute_script("window.scrollTo(0,800)")
finish_button = driver.find_element(By.XPATH,'//button[@id="finish"]')
finish_button.click()


print('TEST COMPLITTED')
driver.close()
