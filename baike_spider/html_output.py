import requests

header = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive'
}


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        # fout = open('output.html', 'w')
        #
        # fout.write("<html>")
        # fout.write("<body>")
        # fout.write("<table>")
        # # ascii
        # for data in self.datas:
        #     fout.write("<tr>")
        #     for img in data:
        #         fout.write("<td><img src=%s></td>" % img)
        #     fout.write("</tr>")
        # fout.write("</table>")
        # fout.write("</body>")
        # fout.write("</html>")
        # fout.close()
        count = 0
        index = 0
        for data in self.datas:
            count = count + 1
            for img in data:
                index = index + 1
                name = img.split('/')[-1]
                img_url = img
                html = requests.get(img_url, headers=header)
                im = html.content
                with open(str(count * 10 + index) + ".jpg", 'wb')as f:
                    f.write(im)
