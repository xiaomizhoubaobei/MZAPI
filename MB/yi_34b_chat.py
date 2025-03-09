"""
这个模块提供了与Yi34BChat 模型的交互接口
"""
from MZAPI.MB.yi_34b_chat import Yi34BChat

def main() -> None:
    """演示Yi34BChat 模型的使用"""

    # 用户AK/SK在以下地址获取：
    # https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application
    model = Yi34BChat("custom_client", "user_ak", "user_sk")
    result = model.get_response("测试文本")
    print(result)


if __name__ == "__main__":
    main()
