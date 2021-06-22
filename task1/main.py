import logging

from common.file_handler import process_file_content
from task1 import config
from task1 import webserver_handler as webserver

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    process_file_content(config.DATA_PATH)
    webserver.start_webserver()


if __name__ == "__main__":
    main()
