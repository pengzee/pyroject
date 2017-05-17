# coding:utf8
import re
import urlparse

from bs4 import BeautifulSoup

page_url = 'http://www.369hi.com/search?q=李毅'


class Parse(object):
    def startParse(self, content):
        if content is None:
            return
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        sub_urls = set()
        img_urls = set()
        # <a href="/p/12421/pu/1" target="_blank">李毅吧丧尸语录，Top50 。15岁以下禁入</a>
        links = soup.find_all('a', href=re.compile(r"/p/\S+/pu/"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            sub_urls.add(new_full_url)
        # < img id = "img" src = "xxx.jpg?kilobug" > 处理 imgs ?kilobug --> ''
        images = soup.find_all('img')
        for img in images:
            url = img['src']
            url.replace('?kilobug', '')
            img_urls.add(url)
            # print 'img: %s' % url
        return sub_urls, img_urls

    def parseImgUrl(self, content):
        if content is None:
            return
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        sub_urls = set()
        # <a href="/p/10863/pu/20">20</a> next_page
        links = soup.find_all('a', href=re.compile(r"/p/\S+/pu/"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            sub_urls.add(new_full_url)
        # < img id = "img" src = "xxx.jpg?kilobug" > 处理 imgs ?kilobug --> ''
        images = soup.find_all('img', id='img')
        for img in images:
            img.replace('?kilobug', '')
        return links, images
