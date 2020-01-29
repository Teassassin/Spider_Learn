from urllib import request, parse

'''
掌握对url进行参数编码的方法
需要使用parse模块
'''

if __name__ == "__main__":
    url = 'https://www.baidu.com/s?'
    wd = input('Input your keyword: ')
    
    # 要想使用data，需要使用字典
    qs = {
        "wd": wd
    }

    # 转换url编码
    qs = parse.urlencode(qs)
    print(qs)

    fullurl = url + qs
    print(fullurl)

    rsp = request.urlopen(fullurl)

    html = rsp.read()

    # 转换回来
    print(parse.unquote(fullurl))