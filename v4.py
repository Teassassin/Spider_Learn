import urllib

if __name__ == "__main__":
    url = 'https://www.baidu.com/s?'
    wd = input('Input your keyword: ')
    
    # 要想使用data，需要使用字典
    qs = {
        "wd": wd
    }