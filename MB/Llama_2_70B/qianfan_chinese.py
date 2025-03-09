"""
这个模块提供了Llama-2-70b模型的交互接口
"""

from MZAPI.MB.Llama_2_70B.qianfan_chinese import Qianfan_Chinese


def main() -> None:
    """演示Llama-2-70b模型的使用"""

    # 用户AK/SK在以下地址获取：
    # https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application
    model = Qianfan_Chinese("custom_client", "user_ak", "user_sk")
    result = model.get_response("测试文本")
    print(result)


if __name__ == "__main__":
    main()
    