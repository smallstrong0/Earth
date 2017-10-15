#! /usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient

from tornado.options import define, options

define("port", default=8001, help="run on the given port ", type=int)
define("log_path", default='/tmp', help="log path ", type=str)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # 接受GET的请求
        headers = self.request.headers
        for k, v in headers.items():
            print k, v
        greeting = self.get_argument('greeting', 'Hello')
        self.write('%s , friendly user! %s ' % (greeting, headers))

    def write_error(self, status_code, **kwargs):
        self.write('Holly Shit Error %s' % status_code)


if __name__ == "__main__":
    # 启动tornado实例
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
