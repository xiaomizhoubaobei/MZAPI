# 百度AI地址识别

## 简介
`BaiduAddressRecognition` 是一个 Python 类，用于通过百度 AI 服务识别文本中的地址信息，并进行性能监控和日志记录。

## 功能
- **发送HTTP请求**：向指定的网络地址发送GET请求。
- **记录日志**：自动记录每次请求的详细信息，包括时间戳和服务器响应。
- **分布式追踪**：使用OpenTelemetry技术，帮助您追踪请求的路径。
- **IP追踪**：记录发起请求的公网IP地址。 

## 安装步骤
在开始使用`BaiduAddressRecognition`之前，您需要确保已经安装了所有必要的依赖库。请按照以下步骤操作：

1. 打开您的命令行工具（例如，终端或命令提示符）。
2. 输入以下命令并按回车：

   ```bash
   pip install MZAPI
   ```
   这个命令会安装`BaiduAddressRecognition`所需的所有库。

## 使用方法 .

### 步骤1 ：导入库 
```python
from MZAPI.bdai import BaiduAddressRecognition
```

这行代码告诉Python去哪里找到`BaiduAddressRecognition`函数。

### 步骤2 ：初始化类
```python
M = BaiduAddressRecognition.BaiduAddressRecognition("你的AK", "你的SK", "自定义客户端名")
```

这行代码会创建一个`BaiduAddressRecognition`类的实例，并传入您的百度AI服务的AK、SK和自定义客户端名。

### 步骤3 ：调用方法
```python
response = M.recognize("你要识别的文本")
```

这行代码会调用`BaiduAddressRecognition`类的`recognize`方法，并传入您要识别的文本。该方法会返回一个包含识别结果的响应对象。

### 步骤4 ：处理响应
```python
print(response)
```
完整源码见[BaiduAddressRecognition.py](../examples/BaiduAddressRecognition.py)

这行代码会打印出响应对象的内容，您可以根据需要进一步处理这些信息。

## 响应示例
```json
{
  "id": 1734012003,
  "traceID": "5b82306ccbcd4d249edae6a3dc25c026",
  "time": "2024-12-12 22:00:03",
  "response": {
    "lat": 31.185795,
    "detail": "纳贤路701号百度上海研发中心F4A000",
    "town": "张江镇",
    "phonenum": "",
    "city_code": "310100",
    "province": "上海市",
    "person": "张三",
    "lng": 121.612334,
    "province_code": "310000",
    "text": "上海市浦东新区纳贤路701号百度上海研发中心 F4A000 张三",
    "county": "浦东新区",
    "city": "上海市",
    "county_code": "310115",
    "town_code": "310115125",
    "log_id": 1867208113917133354
  }
}
```

### 响应字段说明
- `id`：请求的唯一标识符。
- `traceID`：分布式追踪的ID，用于追踪请求的路径。
- `time`：请求的时间戳。
- `response`：包含识别结果的字典。
  - `lat`：纬度。
  - `detail`：详细地址。
  - `town`：乡镇。
  - `phonenum`：电话号码。
  - `city_code`：城市代码。
  - `province`：省份。
  - `person`：人名。
  - `lng`：经度。
  - `province_code`：省份代码。
  - `text`：原始文本。
  - `county`：县区。
  - `city`：城市。
  - `county_code`：县区代码。
  - `town_code`：乡镇代码。
  - `log_id`：日志ID。

## 分布式追踪
`BaiduAddressRecognition`类使用OpenTelemetry技术进行分布式追踪。这意味着您可以通过`traceID`字段追踪请求的路径，了解请求是如何在不同服务之间传递的。
## IP追踪
`BaiduAddressRecognition`类会自动记录发起请求的公网IP地址，帮助您了解请求的来源。
## 性能监控
`BaiduAddressRecognition`类会自动记录每次请求的详细信息，包括时间戳和服务器响应，帮助您监控请求的性能。
## 日志记录
`BaiduAddressRecognition`类会自动记录每次请求的详细信息，包括时间戳和服务器响应，帮助您了解请求的来源和性能。
## 注意事项
在使用`BaiduAddressRecognition`类时，请确保您已经正确安装了所有必要的依赖库，并且已经正确配置了百度AI服务的AK和SK。如果您遇到任何问题，请参考官方文档或联系技术支持。
## 联系方式
如果您在使用`BaiduAddressRecognition`类时遇到任何问题，或者有任何建议或意见，请随时联系我们的技术支持团队。
## 版权信息
本项目的所有代码和文档均受版权保护。未经许可，不得复制、分发或以其他方式使用本项目的任何部分。
## 免责声明
本项目的所有代码和文档仅用于学习和研究目的。我们不承担任何因使用本项目的代码和文档而导致的任何责任或损失。