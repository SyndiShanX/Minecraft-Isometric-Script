import subprocess, shutil, os
from os import path
from shutil import copyfile

fileDir = os.getcwd()
fileDir = fileDir.replace('\\', '/')
fileDir = fileDir + '/Isometrics/'

if path.exists('Isometrics'):
  shutil.rmtree('Isometrics')
  os.mkdir('Isometrics')

textureList = os.listdir('Textures')
texturesXML = [file for file in textureList if file.endswith('.png')]
textureNum = len(texturesXML)

i = 0

while i <= textureNum:
  textureCount = len(texturesXML)
  if textureCount != 0:
    currentTexture = 'Textures\\' + texturesXML[0]
    
    copyfile(currentTexture, 'Texture.png')
    
    subprocess.call('blender -b Isometric_Block_Batch.blend -o ' + fileDir + ' -f 1')
    
    os.rename('Isometrics\\0001.png','Isometrics\\Isometric_' + str(i) + '.png')
    
    texturesXML.remove(texturesXML[0])
    
    i = i + 1
  if path.exists('Texture.png'):
    os.remove('Texture.png')
