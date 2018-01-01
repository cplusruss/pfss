#! -*- coding: utf-8 -*-

import pyglet
import sys

from time import sleep

def main():
    filename = './assets/pfss_perrier.m4a'

    music = pyglet.media.load(filename, streaming=False)
    music.play()

    sleep(music.duration)

main()
