import requests

header = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive'
}


class OutPut(object):
    def startOutput(self, imgs):
        count = 0
        for data in imgs:
            count = count + 1
            html = requests.get(data, headers=header)
            im = html.content
            with open(str(count) + ".jpg", 'wb')as f:
                f.write(im)
