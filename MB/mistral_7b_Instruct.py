"""
这个模块提供了与Mixtral-7B-Instruct模型的交互接口
"""
from MZAPI.MB.mistral_7b_Instruct import Mixtral_7B_Instruct

def main() -> None:
    """演示Mixtral-7B-Instruct模型的使用"""

    # 用户AK/SK在以下地址获取：
    # https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application
    model = Mixtral_7B_Instruct("custom_client", "user_ak", "user_sk")
    result = model.get_response("测试文本")
    print(result)


if __name__ == "__main__":
    main()
    