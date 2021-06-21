from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from task2.stores_handler import filter_store
import logging

from task2 import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class StoreHandler(RequestHandler):
    def get(self):
        find = self.get_argument("find", None, True)
        self.write({"results": filter_store(find)})


def make_app():
    urls = [("/filter", StoreHandler)]
    return Application(urls)


if __name__ == '__main__':
    logger.info(f"The server is listening on port {config.WEBSERVER_PORT}")
    logger.info(f"Example call: http://localhost:{config.WEBSERVER_PORT}/filter?find=hav")
    app = make_app()
    app.listen(config.WEBSERVER_PORT)
    IOLoop.instance().start()
