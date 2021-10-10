from shape_panels import refresh_all as refresh_all_panels
from shapes import refresh_all as refresh_all_shapes

from threading import Thread
from time import sleep


def refresh_all():
    while True:
        try:
            refresh_all_shapes()
            refresh_all_panels()
            sleep(0.2)
        except RuntimeError:
            break


def trigger():
    Thread(target=refresh_all).start()
