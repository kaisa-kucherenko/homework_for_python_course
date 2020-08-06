import logging


class MyLogger(logging.getLoggerClass()):
    Levels = {'DEBUG': 10,
              'INFO': 20, 'WARNING': 30,
              'ERROR': 40, 'CRITICAL': 50}

    def __init__(self, name, logger_level='DEBUG', fh_level='WARNING',
                 sh_level='INFO'):
        self.name = name
        self._logger_level = self.logger_level = logger_level
        self._fh_level = self.fh_level = fh_level
        self._sh_level = self.sh_level = sh_level
        super().__init__(self.name)
        self.addHandler(self._file_handler())
        self.addHandler(self._stream_handler())

    @property
    def logger_level(self):
        return self._logger_level

    @logger_level.setter
    def logger_level(self, level):
        if self.Levels.get(level.upper()):
            self._logger_level = self.Levels[level.upper()]
        else:
            self._logger_level = 10

    @property
    def fh_level(self):
        return self._fh_level

    @fh_level.setter
    def fh_level(self, level):
        if self.Levels.get(level.upper()):
            self._fh_level = self.Levels[level.upper()]
        else:
            self._fh_level = 10

    @property
    def sh_level(self):
        return self._sh_level

    @sh_level.setter
    def sh_level(self, level):
        if self.Levels.get(level.upper()):
            self._sh_level = self.Levels[level.upper()]
        else:
            self._sh_level = 0

    def _file_handler(self):
        fh = logging.FileHandler(f'{self.name}.log')
        fh.setLevel(self.fh_level)
        fh.setFormatter(self.formatter())
        return fh

    def _stream_handler(self):
        sh = logging.StreamHandler()
        sh.setLevel(self.sh_level)
        sh.setFormatter(self.formatter())
        return sh

    @staticmethod
    def formatter():
        formatter = logging.Formatter(f'%(levelname)s: %(message)s - '
                                      '[Func name: %(funcName)s] - '
                                      '[Line: %(lineno)d] - '
                                      '[Time: %(asctime)s]')
        return formatter


if __name__ == '__main__':
    logger = MyLogger(__name__)
