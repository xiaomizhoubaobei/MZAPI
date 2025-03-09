"""
这个模块提供了与ERNIE-Lite-8K模型的交互接口
"""
from MZAPI.MB.lite_8k import Lite_8K


def main() -> None:
    """演示ERNIE-Lite-8K模型的使用"""

    # 用户AK/SK在以下地址获取：
    # https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application
    model = Lite_8K("custom_client", "user_ak", "user_sk")
    result = model.get_response("测试文本")
    print(result)


if __name__ == "__main__":
    main()
    