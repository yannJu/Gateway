from subprocess  import call
import os
import picamera

def convert(src, dst):
    command =  f'MP4Box -add {src} {dst}'
    call([command], shell = True)
    os.remove(src)