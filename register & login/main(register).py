from Utils import *

#valid test
# user_name = "daniel"
# user_LastName = "asas"
# url_profile_pic = "asxasc"
# url_cover_pic = "file:///Users/dnylgmbr/Desktop/one/17354.webp"
# Emil = "dj@mac.com"
# contry = "zxc"
# city = "zxc"
# password = "123456"
# conf_password = "123456"
#
# driver = Cheak()
# driver.test_register(user_name,user_LastName,url_profile_pic,url_cover_pic,Emil,contry,city,password,conf_password)

# driver.test_ui_signup()


# #invalid test username null
user_name = "hfc"
user_LastName = "fyxh"
Url_profile_pic = "asxasc"
Url_cover_pic = "file:///Users/dnylgmbr/Desktop/one/17354.webp"
Emil = "dj@gmail.com"
contry = "zxc"
city = "zxc"
password = "123456"
conf_password = "123456"

driver = Cheak()
driver.test_register(user_name,user_LastName,Url_profile_pic,Url_cover_pic,Emil,contry,city,password,conf_password)

#invalid test userlastname null
# user_name = "daniel"
# user_LastName = ""
# Url_profile_pic = "asxasc"
# Url_cover_pic = "file:///Users/dnylgmbr/Desktop/one/17354.webp"
# Emil = "dj@mac.com"
# contry = "zxc"
# city = "zxc"
# password = "123456"
# conf_password = "123456"
#
# driver = Cheak()
# driver.test_register(user_name,user_LastName,Url_profile_pic,Url_cover_pic,Emil,contry,city,password,conf_password)
#
#
# #invalid test profile pic null
# user_name = "daniel"
# user_LastName = "asas"
# Url_profile_pic = ""
# Url_cover_pic = "file:///Users/dnylgmbr/Desktop/one/17354.webp"
# Emil = "dj@mac.com"
# contry = "zxc"
# city = "zxc"
# password = "123456"
# conf_password = "123456"
#
# driver = Cheak()
# driver.test_register(user_name,user_LastName,Url_profile_pic,Url_cover_pic,Emil,contry,city,password,conf_password)
#
# #invalid test cover pic null
# user_name = "dani"
# user_LastName = "asas"
# Url_profile_pic = "asxasc"
# Url_cover_pic = ""
# Emil = "dj@mac.com"
# contry = "zxc"
# city = "zxc"
# password = "123456"
# conf_password = "123456"
#
# driver = Cheak()
# driver.test_register(user_name,user_LastName,Url_profile_pic,Url_cover_pic,Emil,contry,city,password,conf_password)
#
# #invalid test email null
# user_name = "daniel"
# user_LastName = "asas"
# Url_profile_pic = "asxasc"
# Url_cover_pic = "file:///Users/dnylgmbr/Desktop/one/17354.webp"
# Emil = ""
# contry = "zxc"
# city = "zxc"
# password = "123456"
# conf_password = "123456"
#
# driver = Cheak()
# driver.test_register(user_name,user_LastName,Url_profile_pic,Url_cover_pic,Emil,contry,city,password,conf_password)
#
#
# #invalid test contry null
# user_name = "dan"
# user_LastName = "asas"
# Url_profile_pic = "asxasc"
# Url_cover_pic = "file:///Users/dnylgmbr/Desktop/one/17354.webp"
# Emil = "dj@mac.com"
# contry = ""
# city = "zxc"
# password = "123456"
# conf_password = "123456"
#
# driver = Cheak()
# driver.test_register(user_name,user_LastName,Url_profile_pic,Url_cover_pic,Emil,contry,city,password,conf_password)
#
# #invalid test city null
# user_name = "dan"
# user_LastName = "asas"
# Url_profile_pic = "asxasc"
# Url_cover_pic = "file:///Users/dnylgmbr/Desktop/one/17354.webp"
# Emil = "dj@mac.com"
# contry = "spain"
# city = ""
# password = "123456"
# conf_password = "123456"
#
# driver = Cheak()
# driver.test_register(user_name,user_LastName,Url_profile_pic,Url_cover_pic,Emil,contry,city,password,conf_password)
#
#
# #invalid test password null
# user_name = "dan"
# user_LastName = "asas"
# Url_profile_pic = "asxasc"
# Url_cover_pic = "file:///Users/dnylgmbr/Desktop/one/17354.webp"
# Emil = "dj@mac.com"
# contry = "spain"
# city = "lkfnbs"
# password = ""
# conf_password = "123456"
#
# driver = Cheak()
# driver.test_register(user_name,user_LastName,Url_profile_pic,Url_cover_pic,Emil,contry,city,password,conf_password)
#
#
# #invalid test confim password null
# user_name = "dan"
# user_LastName = "asas"
# Url_profile_pic = "asxasc"
# Url_cover_pic = "file:///Users/dnylgmbr/Desktop/one/17354.webp"
# Emil = "dj@mac.com"
# contry = "spain"
# city = "dkfnbmsl"
# password = "123456"
# conf_password = ""
#
# driver = Cheak()
# driver.test_register(user_name,user_LastName,Url_profile_pic,Url_cover_pic,Emil,contry,city,password,conf_password)





# def test_signup():
#     driver = init()
#     driver.find_element(By.XPATH, "//input[@placeholder='User Name']").send_keys(user_name)
#     driver.find_element(By.XPATH, "//input[@placeholder='User Last Name']").send_keys(user_LastName)
#     driver.find_element(By.XPATH, "//input[@placeholder='User Profile picture']").send_keys(url_profile_pic)
#     driver.find_element(By.XPATH, "//input[@placeholder='cover Picture']").send_keys(url_cover_pic)
#     driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys(Emil)
#     driver.find_element(By.XPATH, "//input[@placeholder='Country']").send_keys(contry)
#     driver.find_element(By.CSS_SELECTOR, "input[placeholder='City']").send_keys(city)
#     driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(password)
#     driver.find_element(By.CSS_SELECTOR, "input[placeholder='PasswordConfirm']").send_keys(conf_password)
#     sleep(3)
#     driver.find_element(By.XPATH,"//button[@type='submit']").click()
#     sleep(3)
#     logout = driver.find_element(By.CLASS_NAME, "MuiButton-label").get_attribute("innerText")
#     assert logout == "LOGOUT"
#     driver.close()
#
#
#
# def test_login():
#     driver = init()
#     driver.find_element(By.XPATH,"//button[@class='loginRegisterButton']").click()
#     driver.find_element(By.XPATH,"//input[@placeholder='Email']").send_keys(Emil)
#     driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys(password)
#     driver.find_element(By.XPATH,"//button[@class='loginButton']").click()
#     sleep(3)
#     logout = driver.find_element(By.CLASS_NAME,"MuiButton-label").get_attribute("innerText")
#     assert logout == "LOGOUT"
#     driver.close()