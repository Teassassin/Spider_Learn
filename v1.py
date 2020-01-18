from urllib import request

'''
    使用urllib.request请求一个网页内容，并把内容打印出来
'''

if __name__ == '__main__':
    url = "https://space.bilibili.com/177736050/favlist?fid=722785850&ftype=create"

    # 打开相应url并把相应页面作为返回
    rsp = request.urlopen(url)

    # 把返回结果读取出来
    html = rsp.read()
    # print(type(html))
    # read()之后的类型是bytes，需要用decode转换成字符串
    html = html.decode()

    print(html)