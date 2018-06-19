# coding = utf-8

import time
import get_webdriver
import web_login
import add_goods

# 获取webdriver
browser = get_webdriver.get_webdriver_of_Chrome()

# 登录
web_login.phone_login(browser)

time.sleep(3)

# 添加货品
add_goods.add_goods(browser)



