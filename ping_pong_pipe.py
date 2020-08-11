from multiprocessing import Process, Pipe
from time import sleep
from os import getpid


def ponger(connection, response):
    while True:
        msg = connection.recv()
        print(f"Process{getpid()} got message: {msg}")
        sleep(2)
        connection.send(response)


if __name__ == "__main__":
    ping, pong = Pipe()
    process1 = Process(target=ponger, args=(ping, 'Pong'))
    process2 = Process(target=ponger, args=(pong, 'Ping'))
    process1.start()
    process2.start()
    pong.send('Ping')
