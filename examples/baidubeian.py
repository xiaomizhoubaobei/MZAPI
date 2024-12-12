# 导入BAIDU类
from MZAPI.bdbeian import BAIDU

# 创建BAIDU对象，传入自定义客户端名称
M = BAIDU("自定义客户端名称")

# 调用get_response方法，传入需要查询的域名
X = M.get_response("需要查询的域名")

# 打印查询结果
print(X)
