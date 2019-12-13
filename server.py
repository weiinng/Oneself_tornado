import tornado.ioloop
import tornado.httpserver
import config

from application import Application




if __name__ == "__main__":
    print('启动...')
    app = Application()
    httpServer = tornado.httpserver.HTTPServer(app,max_buffer_size=504857600)
    # httpServer.listen(8888)
    #绑定端口
    httpServer.bind(config.options['port'])
    #开启5个子进程（默认1，若为None或者小于0，开启对应硬件的CPU核心数个子进程）
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()