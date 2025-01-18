"""
这个模块提供了一个简单的接口来与ERNIE-4.0-Turbo-8K-latest模型进行交互。
它允许用户通过提供文本输入来获取模型的响应。
"""

from MZAPI.MB.ERNIE40.Turbo_8K_latest import Turbo_8K_latest

def main():
    """
    主函数，用于演示如何使用ERNIE-4.0-Turbo-8K-latest模型。

    它创建了一个EightK模型的实例，将测试文本传递给它，
    并打印出模型的响应。
    """
    # 用户AK和SK在https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application中获取
    model = Turbo_8K_latest("自定义客户端名称", "用户AK", "用户SK")
    result = model.get_response("测试文本")
    print(result)

if __name__ == "__main__":
    main()
