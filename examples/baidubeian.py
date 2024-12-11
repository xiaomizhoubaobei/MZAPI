from MZAPI.bdbeian import BAIDU


def W():
    M = BAIDU("XMZ")
    X = M.get_response("www.baidu.com")
    print(X)


if __name__ == "__main__":
    W()
