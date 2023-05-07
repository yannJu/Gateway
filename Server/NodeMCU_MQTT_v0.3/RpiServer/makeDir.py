import subprocess
import os

def mkdir(src):
    # src 의 파일을 dst 로 변환
    cmd = f'mkdir {src}'
    subprocess.call([cmd], shell = True)