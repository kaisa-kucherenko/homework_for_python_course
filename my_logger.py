import logging


class MyLogger(logging.Logger):
    Levels = {'DEBUG': 10,
              'INFO': 20, 'WARNING': 30,
              'ERROR': 40, 'CRITICAL': 50}

    def __init__(self, name, logger_level='DEBUG', fh_level='WARNING',
                 ch_level='INFO', file_name=None):
        self.name = name
        self._logger_level = self.logger_level = logger_level
        self._fh_level = self.fh_level = fh_level
        self._ch_level = self.ch_level = ch_level
        self._file_name = self.file_name = file_name
        super().__init__(self.name)
        self.addHandler(self._file_handler())
        self.addHandler(self._stream_handler())

    @property
    def logger_level(self):
        return self._logger_level

    @logger_level.setter
    def logger_level(self, level):
        self._logger_level = self.Levels.get(level.upper(), 10)

    @property
    def fh_level(self):
        return self._fh_level

    @fh_level.setter
    def fh_level(self, level):
        self._fh_level = self.Levels.get(level.upper(), 10)

    @property
    def ch_level(self):
        return self._ch_level

    @ch_level.setter
    def ch_level(self, level):
        self._ch_level = self.Levels.get(level.upper(), 10)

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, f_name):
        if f_name is None:
            self._file_name = self.name.lower()
        else:
            self._file_name = str(f_name).lower()

    def _file_handler(self):
        fh = logging.FileHandler(f'{self.file_name}.log')
        fh.setLevel(self.fh_level)
        fh.setFormatter(self.formatter())
        return fh

    def _stream_handler(self):
        ch = logging.StreamHandler()
        ch.setLevel(self.ch_level)
        ch.setFormatter(self.formatter())
        return ch

    @staticmethod
    def formatter():
        formatter = logging.Formatter(f'%(levelname)s: %(message)s - '
                                      '[Logger name: %(name)s] - '
                                      '[Func name: %(funcName)s] - '
                                      '[Line: %(lineno)d] - '
                                      '[Time: %(asctime)s]')
        return formatter


if __name__ == '__main__':
    logger = MyLogger(__name__)
