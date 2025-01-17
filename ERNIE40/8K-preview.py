from  MZAPI.MB.ERNIE40.EightK_preview import EightK_preview


def main():
    #用户AK和SK在https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application中获取
    model = EightK_preview("自定义客户端名称", "用户AK", "用户SK")
    result = model.get_response("测试文本")
    print(result)

if __name__ == "__main__":
    main()