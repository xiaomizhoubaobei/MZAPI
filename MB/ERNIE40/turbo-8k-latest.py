"""
这个模块提供了ERNIE-4.0-Turbo-8K-latest模型的交互接口
"""

from MZAPI.MB.ERNIE40.turbo_8k_latest import Turbo_8K_latest


def main() -> None:
    """演示ERNIE-4.0-Turbo-8K-latest模型的使用"""

    # 用户AK/SK在以下地址获取：
    # https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application
    model = Turbo_8K_latest("custom_client", "user_ak", "user_sk")
    result = model.get_response("测试文本")
    print(result)


if __name__ == "__main__":
    main()
