# codeing = utf-8

from selenium.webdriver.support.ui import Select

import time
import win32gui
import win32con

def add_goods(browser):
    # 切换到商品列表
    browser.get("http://s.100svip.com/#/index/shopping/productList1")

    # 添加商品
    good_name = "安踏男鞋跑步鞋"

    colors = ["深蓝", "荧光绿"]
    sizes = ["41", "42", "42.5"]
    unit_name = "件"
    pictures_path = "C:\\Users\\rehai\\Pictures\\商城商品信息\\"
    picture_suffix = r".jpg"
    files_names = ["1601", "1602", "1603", "1604"]

    colors_len = len(colors)
    sizes_len = len(sizes)

    line_num = colors_len * sizes_len


    # 点击新增按钮
    browser.find_element_by_class_name("col-md-12").find_element_by_css_selector("#page-wrapper > div:nth-child(2) > div > div.row.minor-content2.minw > div.col-md-12 > div.col-md-4.col-sm-4.col-xs-4.line > div > button.btn.btn-increase").click()
    time.sleep(3)

    good_content = browser.find_element_by_class_name("xinzeng-content")

    # 输入商品名称
    good_content.find_element_by_css_selector("#xinzeng > div:nth-child(2) > div > div:nth-child(1) > div:nth-child(1) > input").send_keys(good_name)

    # 选择货品单位
    select_list_selector_one = good_content.find_element_by_css_selector("#xinzeng > div:nth-child(2) > div > div:nth-child(1) > div:nth-child(2) > select")
    select_list_one = Select(select_list_selector_one)
    select_list_one.select_by_visible_text(unit_name)

    # 选择货品类别
    select_list_selector_two = good_content.find_element_by_css_selector("#xinzeng > div:nth-child(2) > div > div:nth-child(1) > div.right.input-area > select")
    select_list_two = Select(select_list_selector_two)
    select_list_two.select_by_index(1)

    # 设置商品多项
    new_add_button = good_content.find_element_by_xpath("//*[@id='xinzeng']/div[2]/div/div[2]/div[3]/button")


    # 填写货品表格
    good_details_table = good_content.find_element_by_class_name("tbody")
    for lineNum in range(0, line_num):
        good_details_table.find_element_by_css_selector("#txt > tr:nth-child(" + str(lineNum + 1) + ") > td:nth-child(3) > input").send_keys(colors[lineNum % colors_len])
        good_details_table.find_element_by_css_selector("#txt > tr:nth-child(" + str(lineNum + 1) + ") > td:nth-child(4) > input").send_keys(sizes[lineNum % sizes_len])
        good_details_table.find_element_by_css_selector("#txt > tr:nth-child(" + str(lineNum + 1) + ") > td:nth-child(6) > input").send_keys("10")
        good_details_table.find_element_by_css_selector("#txt > tr:nth-child(" + str(lineNum + 1) + ") > td:nth-child(7) > input").send_keys("10")
        good_details_table.find_element_by_css_selector("#txt > tr:nth-child(" + str(lineNum + 1) + ") > td:nth-child(8) > input").send_keys("15")
        good_details_table.find_element_by_css_selector("#txt > tr:nth-child(" + str(lineNum + 1) + ") > td:nth-child(9) > input").send_keys("168")
        good_details_table.find_element_by_css_selector("#txt > tr:nth-child(" + str(lineNum + 1) + ") > td:nth-child(10) > input").send_keys("25")
        good_details_table.find_element_by_css_selector("#txt > tr:nth-child(" + str(lineNum + 1) + ") > td:nth-child(11) > input").send_keys("1000")
        good_details_table.find_element_by_css_selector("#txt > tr:nth-child(" + str(lineNum + 1) + ") > td:nth-child(12) > input").send_keys("100")
        
        if (lineNum + 1) == line_num:
            break
        else:
            new_add_button.click()


    # 设置图片按钮
    browser.find_element_by_class_name("xinzeng-herder").find_element_by_css_selector("#xinzeng > div.xinzeng-herder > button.btn.btn-shezhi.shezhi-colors").click()

    # 设置图片区域selector
    picture_settings = browser.find_element_by_class_name("layui-layer-content")
    time.sleep(2)

    # 添加图片文件
    for picNum in range(0, line_num):
        upload = picture_settings.find_element_by_xpath("//*[@id='xinzeng']/div[3]/div[" + str(picNum + 1) + "]/div/input")
        upload.click()
        time.sleep(2)
        # win32gui
        dialog = win32gui.FindWindow('#32770', u'打开')  # 对话框
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None) 
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
        time.sleep(2)

        picture_path = pictures_path + files_names[picNum % len(files_names)] + picture_suffix;
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, picture_path)  # 往输入框输入绝对地址
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
        time.sleep(2)

    save_button = browser.find_element_by_class_name("layui-layer-btn0")
    save_button.click()