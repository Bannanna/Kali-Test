# import re
# import os
# import sh
# import subprocess
# def shProcess(files):
# def config_make_install(dir='./', filelist=None):
#     if not filelist:
#         sh.cd(dir)
#         for file in os.listdir(dir):
#             unpackedfile = file[0:file.indexof('.tar')
#             if file.endswith('.gz') || file.endswith('.bz2'):
#                 sh.cd(unpackedfile)
#                 subprocess.call('./configure')
#                 sh.make()
#                 subprocess.Popen(['sudo', 'make', 'install'], shell=True, stdin=subprocess.PIPE,
#                                                                           stdout=subprocess.PIPE,
#                                                                           stderr=subprocess.PIPE)
#                 sh.cd('../')
#                 print '{} installed'.format(file)
#     else:
#         sh.cd(dir)
#         for file in os.listdir('./'):
#             for item in filelist:
#                 if str(item) == file:
#                     sh.cd(file)
#                     subprocess.call('./configure')
#                     sh.make()
#                     print 'Made\ {0}r\n\r\n\r\n\r\n'.format(file)
#                     subprocess.Popen(['sudo', 'make', 'install'], shell=True, stdin=subprocess.PIPE,
#                                                                               stdout=subprocess.PIPE,
#                                                                               stderr=subprocess.PIPE)
#                     sh.cd('../')
#                     print '{} installed'.format(file)
#
# if __name__ == '__main__':
#     config_make_install()
