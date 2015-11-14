##SUDO HANGS!!!
##make bash script accpet filelist as arguments

import re
import os
import sh
import subprocess

##this is g2g except sudo hangs
# for file in os.listdir('./'):
#     if file.startswith('lib'):
#         sh.cd(file)
#         subprocess.call('./configure')
#         sh.make()
#         subprocess.Popen('sudo make install', shell=True)
#         sh.cd('../')
#         print '{} installed'.format(file)
# def cmdseq():
#     sh.cd(file)
#     subprocess.call('./configure')
#     sh.make()
#     subprocess.Popen(['sudo', 'make', 'install'], shell=True, stdin=subprocess.PIPE,
#                                                               stdout=subprocess.PIPE,
#                                                               stderr=subprocess.PIPE)
#     sh.cd('../')
tar = sh.Command('tar')
def fab(call=None, p=None):
    if not call:
        print 'Fatal'
        exit()
    else:
        if not p:
            return subprocess.call(call, shell=True)
        if p:
            return subprocess.call(call, shell=True, stdin=subprocess.PIPE,
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
def tarutil(flags='', archivo='man', dldir='../../downloads'):
    sh.cd(dldir)
    if archivo=='man':
        fab(call='man man')
    elif not archivo=='man':
        ac = str(archivo)
        if ac.endswith('.bz2'):
            print 'taring ' + ac
            # fab(call='tar -xvf ./{}'.format(archivo))
        elif ac.endswith('.tar.gz'):
            # fab(call='tar -xvf ./{}'.format(archivo))
            print 'tarring ' + ac
        else:
            print('fatal, not a tarable file')
            exit()

def config_make_install(dir='downloads', filelist=None):
    download_list = os.listdir(dir)
    if not download_list:
        print 'fatal no files in download_list'
        exit()
    if len(download_list) < 1:
        print 'must download first'
    elif download_list:
        sh.cd(dir)
        for file in os.listdir('./'):
            if file.endswith('.tar.gz') or file.endswith('.tar.bz2'):
                sh.cd(file)
                subprocess.Popen(['./config && make && make install'], shell=True, stdin=subprocess.PIPE,
                                                                          stdout=subprocess.PIPE)                                                                          stderr=subprocess.PIPE)
                sh.cd('../')
                print '{} configed, made, installed'.format(file)

if __name__ == '__main__':
    import parsethtml
    tarutil()
    config_make_install(dir='./downloads')
