"""
这个模块提供了ERNIE-4.0-Turbo-8K模型的交互接口
"""

from MZAPI.MB.ERNIE40.turbo_8k import Turbo_8K


def main() -> None:
    """演示ERNIE-4.0-8K-Turbo-8K模型的使用"""

    # 用户AK/SK在以下地址获取：
    # https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application
    model = Turbo_8K("custom_client", "user_ak", "user_sk")
    result = model.get_response("测试文本")
    print(result)


if __name__ == "__main__":
    main()
