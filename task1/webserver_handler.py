import pickle

import tornado.escape
import tornado.ioloop
import tornado.locks
import tornado.web
import os.path
import logging

from task1 import config
from tornado.options import options, parse_command_line, define

define("port", default=config.WEBSERVER_PORT, help="run on the given port", type=int)
define("debug", default=True, help="run in debug mode")

logger = logging.getLogger(__name__)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        with open(config.OUT_PATH, "rb") as f:
            self.render("index.html", stores=pickle.load(f))


def start_webserver():
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/", MainHandler)
        ],
        cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=True,
        debug=options.debug,
    )
    app.listen(options.port)
    logger.info(f"The server is listening on port {config.WEBSERVER_PORT}")
    logger.info(f"Please open http://localhost:{config.WEBSERVER_PORT}")
    tornado.ioloop.IOLoop.current().start()
