from urllib import request


if __name__ == '__main__':
    url = "https://space.bilibili.com/177736050/favlist?fid=722785850&ftype=create"

    rsp = request.urlopen(url)

    print(type(rsp))
    print(rsp)

    print("URL: {0}".format(rsp.geturl()))
    print("Info: {0}".format(rsp.info()))
    print("Code: {0}".format(rsp.getcode()))

    html = rsp.read()
    html = html.decode()

    # print(html)