# BAIDU SDK 使用指南

## 这是什么？
这个SDK可以帮助您查询网站的ICP备案信息，并把结果告诉您。

## 我需要什么？
- Python环境
- 网络连接

## 如何使用？

1. **创建BAIDU查询对象**：
   - 打开您的Python文件，导入`BAIDU`类，并创建一个对象。
     ```python
     from MZAPI.bdbeian import BAIDU

     # 替换为您的客户端名称
     my_baidu = BAIDU("my_client_name")
     ```

2. **查询ICP备案信息**：
   - 使用您创建的对象来查询网站的ICP备案信息。
     ```python
     # 替换为您要查询的网站域名
     domain = "example.com"
     result = my_baidu.get_response(domain)
     print(result)
     ```

3. **查看结果**：
   - 上述代码会打印出一个包含查询结果的字典，里面会有您需要的所有信息。

4.**完整源码**
   - 完整源码请参见[baidubeian.py](../examples/baidubeian.py)文件。


## 响应示例

假设您已经运行了`get_response`方法，并且成功地从百度ICP查询接口获取了数据，以下为响应示例：

```json
{
  "id": 1733813109,
  "traceID": "eaacee20da9a8cfbae7ed45ed7bf75f2",
  "time": "2024-12-10 14:45:09",
  "response": {
    "code": 1,
    "message": "Success/获取成功",
    "data": {
      "auditTime": "2019-05-16 00:00:00",
      "company": "北京百度网讯科技有限公司",
      "domain": "www.baidu.com",
      "exists": true,
      "number": "京ICP证030173号-1",
      "siteName": "百度",
      "type": "enterprise"
    }
  }
}
```

## 响应内容解释

- **id**: 请求的唯一标识符，通常是UNIX时间戳。
- **traceID**: 跟踪ID，用于在APM系统中追踪请求。
- **time**: 请求发送的时间，格式为`YYYY-MM-DD HH:MM:SS`。
- **response**: 包含响应结果的JSON对象，具体内容如下：
  - **code**: 响应代码，1表示成功。
  - **message**: 响应消息，表示查询结果的状态。
  - **data**: 包含查询结果的JSON对象，具体内容如下： 
    - **auditTime**: 备案审核时间。
    - **company**: 备案主体名称。
    - **domain**: 查询的网站域名。
    - **exists**: 是否存在备案信息，true表示存在。
    - **number**: ICP备案号。
    - **siteName**: 网站名称。
    - **type**: 备案类型，enterprise表示企业网站。

## 如何使用响应数据

您可以根据需要处理这些数据，例如：

1. **检查备案状态**：
   ```python
   if result["response"]["status"] == "正常":
       print("网站备案状态正常。")
   else:
       print("网站备案状态异常。")
   ```

2. **提取ICP备案号**：
   ```python
   icp_number = result["response"]["icp"]
   print(f"网站的ICP备案号是：{icp_number}")
   ```

3. **记录或显示备案主体信息**：
   ```python
   owner_info = result["response"]["owner"]
   print(f"网站的备案主体是：{owner_info}")
   ```

## 注意事项
- 确保您使用的域名是正确的。
- 如果您在使用过程中遇到任何问题，请检查您的网络连接。

## 常见问题
Q: 我怎么知道查询是否成功？
A: 如果结果中有`response`键，并且包含了很多信息，那么查询就是成功的。

Q: 查询失败怎么办？
A: 请检查您的网络连接，或者稍后再试。

Q: 我需要安装其他软件吗？
A: 不需要，只要您的计算机上安装了Python，就可以使用这个SDK。