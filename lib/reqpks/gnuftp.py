#G2G
# get package names from parsethml.py return value or glob vars
import os

BASE_FTP = 'https://www.gnupg.org'
LOCAL_DIR = './downloads'
REQD_FTP_ROUTES = None

def get_rec_files(base=BASE_FTP, localdir=LOCAL_DIR, recs=REQD_FTP_ROUTES):
    if not recs:
        print 'Must specify url of files to download'
        return
    for r in recs:
        url = base + r
        os.system('wget -P {0} {1}'.format(localdir,url))
        print 'Downloading {0} from {1}'.format(r, url)
    print '\r\n\r\nDownload completed'
