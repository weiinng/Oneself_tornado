import tornado.ioloop
import tornado.httpserver
from views.base import BaseHandler
import tornado.web
import config
import os
import re



#视图函数
class Pushimg(BaseHandler):
    def get(self, *args, **kwargs):
        self.write("你好世界！")


class Save_img(BaseHandler):
    def post(self, *args, **kwargs):
        std = os.popen(
            "docker exec -i storage /usr/bin/fdfs_upload_file /etc/fdfs/client.conf /var/root/test.mp4").read()
        print('*********** fastdfs excute start ***********')
        print(std.strip())
        img_src = std.strip()
        print('*********** fastdfs excute end ***********')




'''--------------------------------------------------------------------------'''
#路由
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/push_img/ceshi",Pushimg),
        ]
        super(Application, self).__init__(handlers, **config.setting)

if __name__ == "__main__":
    print('启动...')
    app = Application()
    httpServer = tornado.httpserver.HTTPServer(app)
    # httpServer.listen(8888)
    #绑定端口
    httpServer.bind(config.options_img['port'])
    #开启5个子进程（默认1，若为None或者小于0，开启对应硬件的CPU核心数个子进程）
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()