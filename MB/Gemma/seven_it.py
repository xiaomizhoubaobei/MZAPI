# -*- coding: utf-8 -*-
"""这个模块提供了Gemma-7B-IT模型的交互接口"""

from MZAPI.MB.Gemma.seven_it import seven_it


def main() -> None:
    """演示Gemma-7B-IT模型的使用"""

    # 用户AK/SK在以下地址获取：
    # https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application
    model = seven_it("custom_client", "user_ak", "user_sk")
    result = model.get_response("测试文本")
    print(result)


if __name__ == "__main__":
    main()
