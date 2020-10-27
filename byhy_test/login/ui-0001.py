from selenium import webdriver
import unittest

# 创建webdriver对象，指明使用chrome浏览器驱动
# ウェブドライバを作成し、chromeドライバ使用を指定する
wd = webdriver.Chrome()

# 打开网址
# アドレスを訪問する
wd.get('http://127.0.0.1/mgr/sign.html')

# 设置最大等待时长
# 最大の待つ時間を設置する
wd.implicitly_wait(10)

# 定位到密码框，并输入密码
# パスワードボックスを探し、バスワードを輸入する
wd.find_element_by_id('password').send_keys('88888888')

# 定位到登录按钮，并点击登录
# ログインボタンを探し、クリックする
wd.find_element_by_css_selector('.btn').click()

# 添加断言，判断弹出窗口的内容是否与预期一致
# 判断を増加し、イジェクトしたのウインドウズの内容は予期通りかどうかをチェックする
# assert wd.switch_to.alert.text == '请输入用户名', '执行失败'
# assert wd.switch_to.alert.text != '请输入用户名', '执行成功'


if wd.switch_to.alert.text == '请输入用户名':
    print('测试通过')
else:
    print('测试失败')



wd.quit()
