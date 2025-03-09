"""
这个模块提供了与Mixtral-8x7B-Instruct模型的交互接口
"""
from MZAPI.MB.mixtral_8x7b_instruct import Mixtral_8x7B_Instruct

def main() -> None:
    """演示Mixtral-8x7B-Instruct模型的使用"""

    # 用户AK/SK在以下地址获取：
    # https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application
    model = Mixtral_8x7B_Instruct("custom_client", "user_ak", "user_sk")
    result = model.get_response("测试文本")
    print(result)


if __name__ == "__main__":
    main()
    