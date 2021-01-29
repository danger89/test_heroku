from logging import info

from src.app import app
from src.urls import init_urls
from src.utils import init_loggers


init_urls(app)
init_loggers()

info('program started')


if __name__ == '__main__':
    # on local
    app.run(threaded=True)

    # import socket
    #
    # sock = socket.socket()
    # print(sock)
    # sock.bind(('localhost', 9090))
    # sock.listen(10)
    # print('listening')
    #
    # conn, addr = sock.accept()
    # print('connect: ', addr)
    #
    # while True:
    #     data = input('>>> ')
    #     conn.send(data.encode())
