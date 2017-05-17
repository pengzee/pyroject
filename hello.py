import web
import MySQLdb
import MySQLdb.cursors
        
urls = (
    '/index', 'index',
    '/blog/\\d+', 'blog',
    '/article', 'article',
    '/(.*)', 'hello',
)
app = web.application(urls, globals())


class index:        
    def GET(self):
        return web.input()

class blog:        
    def GET(self):
        return web.ctx.env
        
    def POST(self):
        return 'blog post method'

class hello:        
    def GET(self, name):
        return open(r'http://www.baidu.com').read()
        
class article:        
    def GET(self):
        conn = MySQLdb.connect(host='192.168.100.36',user='root',passwd='root',db='oa_db',port=3306,cursorclass=MySQLdb.cursors.DictCursor,charset='utf8')
        cur = conn.cursor()
        cur.execute('select * from user')
        r = cur.fetchall()
        cur.close()
        conn.close()
        print r
        return r

if __name__ == "__main__":
    app.run()