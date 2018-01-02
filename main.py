#! -*- coding: utf-8 -*-

import pyglet
import sys

from time import sleep
import sys, getopt


def main(args):
    watertypes = ['perrier', 'topo', 'gerolsteiner', 'lacroix', 'sanpel']

    if (len(args) > 0):
        watertype = args[1]
    else:
        watertype = watertypes[0]
        print 'Specify a water type:' 
        print watertypes


    # Select water type
    filename = './assets/pfss_' + watertype + '.m4a'

    music = pyglet.media.load(filename, streaming=False)
    music.play()

    sleep(music.duration)

if __name__ == "__main__":
    main(sys.argv[1:])
