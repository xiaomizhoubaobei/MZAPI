# 导入百度地址识别模块
from MZAPI.bdai import BaiduAddressRecognition

# 创建百度地址识别对象
M = BaiduAddressRecognition.BaiduAddressRecognition(
    "你的AK", "你的SK", "自定义客户端名称"
)

# 调用识别函数，传入地址字符串
W = M.recognize("上海市浦东新区纳贤路701号百度上海研发中心 F4A000 张三")

# 打印识别结果
print(W)
