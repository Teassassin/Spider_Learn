from urllib import request
import chardet

if __name__ == '__main__':
    url = 'https://tieba.baidu.com/p/5967827433'

    rsp = request.urlopen(url)

    html = rsp.read()

    # 利用chardet自动检测
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    # get()检测到的话将encoding作为键，编码作为值返回，检测不到默认返回utf-8
    html = html.decode(cs.get("encoding", "utf-8"))

    print(html)