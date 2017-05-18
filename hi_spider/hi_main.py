# coding:utf8
from hi_spider import hi_parser, hi_downloader, hi_output, hi_manager


class HiMain(object):
    def __init__(self):
        self.urls = hi_manager.UrlManager()
        self.parser = hi_parser.Parse()
        self.downloader = hi_downloader.Download()
        self.output = hi_output.OutPut()

    def crawRoot(self, root_url):
        print 'root_url: %s' % root_url
        # 遍历 html_cont 中的 item_urls
        html_cont = self.downloader.startDownload(root_url)
        item_urls = self.parser.parseRootPage(html_cont)
        if item_urls is None:
            print ("category content is None !")
            return
        else:
            self.urls.add_new_urls(item_urls)
            self.crawPage()

    def crawPage(self):
        # count = 1
        images = set()
        # 下载 page_url 界面
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
    # root_url = "http://www.369hi.com/p/8328/pu/1"
    root_url = "http://www.369hi.com/category/%E9%AD%94%E5%85%BD%E4%B8%96%E7%95%8C"
    obj_spider = HiMain()
    obj_spider.crawRoot(root_url)
