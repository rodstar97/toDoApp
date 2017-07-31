import os
import glob
from sys import platform

def convert(curDir = ''):
    if platform == 'win32':
        if curDir == '':
            curDir = os.path.dirname(os.path.realpath(__file__))
        print curDir
        os.chdir(curDir)
        os.popen('rm -rf *.pyc')
        uiFiles = glob.glob('{0}/*.ui'.format(curDir))
        for uiFile in uiFiles:
            print os.path.basename(uiFile), '.ui File'
            uiFilewOPath = os.path.basename(uiFile)
            nameWOext = os.path.splitext(os.path.basename(uiFile))
            pyFile = '{0}_ui.py'.format(nameWOext[0])
            print pyFile
            os.popen('c:\Python27\Scripts\pyside-uic.exe -o "{0}" "{1}"'.format(os.path.join(curDir, pyFile), uiFile))
    else:
        if curDir == '':
            curDir = os.path.dirname(os.path.realpath(__file__))
        print curDir
        os.chdir(curDir)
        os.popen('rm -rf *.pyc')
        uiFiles = glob.glob('{0}/*.ui'.format(curDir))
        for uiFile in uiFiles:
            print os.path.basename(uiFile), '.ui File'
            uiFilewOPath = os.path.basename(uiFile)
            nameWOext = os.path.splitext(os.path.basename(uiFile))
            pyFile = '{0}_ui.py'.format(nameWOext[0])
            print pyFile
            os.popen('pyside-uic -o "{0}" "{1}"'.format(os.path.join(curDir, pyFile), uiFile))