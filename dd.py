import io
import logging
from json import dumps
from time import sleep

from flask import Flask
from multiprocessing import Process
from contextlib import contextmanager, redirect_stdout

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


class Server:
    def __init__(self, host, port, data):
        self.__host__ = host
        self.__port__ = port
        self.__data__ = data

    @contextmanager
    def run(self):
        p = Process(target=self.server)
        p.start()
        sleep(1)
        yield
        p.kill()

    def server(self):
        _ = io.StringIO()
        with redirect_stdout(_):
            app = Flask(__name__)

            @app.route('/')
            def index():
                return dumps(self.__data__)

            app.run(self.__host__, self.__port__)


if __name__ == '__main__':
    data = [
        {
            'walk': [211, 197, 243],
            'read': [235, 108, 121, 45],
            'clean': [22, 212, 111],
            'listen': [294, 179, 106]
        },
        {
            'write': [264, 276, 116, 218],
            'listen': [142, 69, 180],
            'admire': [155, 299, 119, 268, 176, 16, 210],
            'read': [233, 195, 282]
        }
    ]

    index = 0
    while (index := int(input('Р’РІРµРґРёС‚Рµ РЅРѕРјРµСЂ РїСЂРёРјРµСЂР°: '))) not in (1, 2):
        ...
    server = Server('127.0.0.1', 8080, data[index - 1])
    with server.run():
        while (row := input('Р’РІРµРґРёС‚Рµ "stop" РґР»СЏ Р·Р°РІРµСЂС€РµРЅРёСЏ СЂР°Р±РѕС‚С‹ СЃРµСЂРІРµСЂР°: ')) != 'stop':
            ...