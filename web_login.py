# codeing = utf-8
import time

def phone_login(browser):

    browser.get("http://s.100svip.com/#/login")

    time.sleep(5)

    # 输入账号
    browser.find_element_by_class_name("value").find_element_by_css_selector("#login_box > div > div.flexbox-box-bd > form > div.form.login > div > div:nth-child(1) > div > input").send_keys("18966666666")

    # 输入密码
    browser.find_element_by_class_name("mobile-layer").find_element_by_css_selector("#login_box > div > div.flexbox-box-bd > form > div.form.login > div > div.row.mb0 > div > input").send_keys("000000")

    # 点击登录
    browser.find_element_by_class_name("submit-layer").find_element_by_xpath("//*[@id='login_box']/div/div[1]/form/div[2]/a").click()


def CAPTCHA_login(browser):
    # TODO: 验证码登录
    pass