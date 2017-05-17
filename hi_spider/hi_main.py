# coding:utf8
from hi_spider import hi_parser, hi_downloader, hi_output, hi_manager


class HiMain(object):
    def __init__(self):
        self.urls = hi_manager.UrlManager()
        self.parser = hi_parser.Parse()
        self.downloader = hi_downloader.Download()
        self.output = hi_output.OutPut()

    def craw(self, root_url):
        print 'root_url: %s' % root_url
        # count = 1
        images = set()
        self.urls.add_new_url(root_url)
        # 下载 root_url 界面
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                html_cont = self.downloader.startDownload(new_url)
                print "new_url: %s" % new_url
                # 遍历 html_cont 中的 sub_urls 和 图片 images
                sub_urls, img_urls = self.parser.startParse(html_cont)
                self.urls.add_new_urls(sub_urls)
                if img_urls is None or len(img_urls) == 0:
                    print 'img_urls is none'
                else:
                    for img in img_urls:
                        if img.endswith('jpg'):
                            images.add(img)
                            # if count == 30:
                            #     break
                            # count = count + 1
            except:
                print 'failed'
        # 下载 图片 到本地硬盘
        print "image length: %s" % len(images)
        self.output.startOutput(images)


if __name__ == "__main__":
    root_url = "http://www.369hi.com/p/8328/pu/1"
    obj_spider = HiMain()
    obj_spider.craw(root_url)
