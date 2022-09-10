import subprocess, os
from os import path

fileDir = os.getcwd()
fileDir = fileDir.replace('\\', '/')
fileDir = fileDir + '/'

fileDir = fileDir + "Texture.png"

if os.path.exists('Isometric.png'):
  os.remove('Isometric.png')

subprocess.call('blender -b Isometric_Block_All.blend -o ' + fileDir + ' -f 1')

os.rename('Texture.png0001.png','Isometric.png')