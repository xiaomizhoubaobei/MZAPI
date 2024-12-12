# 导入WenAnSou类
from MZAPI.wenansou import WenAnSou

# 创建WenAnSou类的实例，传入自定义客户端名称
W = WenAnSou("自定义客户端名称")

# 调用get_response方法，传入要搜索的关键词
M = W.get_response("要搜索的关键词")

# 打印搜索结果
print(M)
