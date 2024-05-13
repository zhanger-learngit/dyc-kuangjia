# 与设备进行连接
# 需要导入uiautomator2三方库
import os

import uiautomator2 as UA

# 需要输入设备的ip地址+端口号
# 连接上以后我们一般会给到一个变量 device
devices = UA.connect('127.0.0.1:21503')
# 可以打印设备信息验证 用来断言
print(devices.device_info)

# 查看页面大小
print(devices.window_size())

# 获取当前当前包名和页面
print(devices.app_current())

# 获取当前app的包名以及所在的页面
# 终端输入uiautomator2 current
# os.system('uiautomator2 current')   不能打印只能执行