"""
这个模块提供了与ChatLaw模型的交互接口
"""
from MZAPI.MB.aquila_7b import ChatLaw


def main() -> None:
    """演示ChatLaw模型的使用"""

    # 用户AK/SK在以下地址获取：
    # https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application
    model = ChatLaw("custom_client", "user_ak", "user_sk")
    result = model.get_response("测试文本")
    print(result)


if __name__ == "__main__":
    main()
    