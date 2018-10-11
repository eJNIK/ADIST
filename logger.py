import logging


class Logger:
    def __init__(self, name='adist_logs', level=logging.DEBUG):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # file_handler = logging.FileHandler('%s.log' % name, 'w')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

        # file_handler.setFormatter(formatter)
        # self.logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)
