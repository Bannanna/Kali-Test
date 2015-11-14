from sh import curl
import argparse

##download kali 2.0-amd64.io and hashes
BASE_URL = 'http://cdimage.kali.org/kali-2.0/'
LOCAL_DIR = '../../downloads'
SHA_SUMS = ['SHA1SUMS', 'SHA1SUMS.gpg']
KALI_ISO = 'kali-linux-2.0-amd64.iso'

def getkali(base=BASE_URL, localdir=LOCAL_DIR, sums=SHA_SUMS, iso=KALI_ISO):
    sh.cd(localdir)
    curl(base, o=iso, silent=False)
    for sum in sums:
        curl(BASE_URL, o=sum, silent=False)
    print '\r\n\r\nDownload completed'

if __name__ == '__main__':
    print 'Not setup as stand-alone module'
    getkali()
    # parser = argparse.ArgumentParser(description='Download kali iso and sums')
    # parser.add_argument('--base')
    # getkali()
