##G2G
import sh
from bs4 import BeautifulSoup

GNU_URL = 'https://www.gnupg.org/download/'
##numbers reefer to major versions
REQD_PKG_NAMES = ['gnupg-2.1', 'libgpg-error-1', 'libgcrypt-1', 'libksba-1']
REQD_FTP_ROUTES = []
#EJEMPLO <a href="/ftp/gcrypt/gnupg/gnupg-2.0.29.tar.bz2">download</a>
def get_file_names(url=GNU_URL):
    html_file = str(sh.curl(url, silent=True))
    parsed_html = BeautifulSoup(html_file, 'html.parser')
    links = parsed_html.body.find_all('a', href=True, text='download')
    all_routes = []
    sig_routes = []
    tar_routes = []
    for a in links:
        strg = str(a)
        if strg.find('tar.bz2') > 1 or strg.find('tar.bz2.sig') > 1:
            for rec in REQD_PKG_NAMES:
                if strg.find(rec) > 1:
                    a['href']
                    all_routes.append(a['href'])
    for rt in all_routes:
        if rt.endswith('.bz2'):
            tar_routes.append(rt)
        elif rt.endswith('.sig'):
            sig_routes.append(rt)
    # print 'Sigs' + str(sig_routes) + '\r\n'
    # print 'Tar' + str(tar_routes) + '\r\n'
    REQD_FTP_ROUTES = sig_routes + tar_routes
    return all_routes, tar_routes, sig_routes

if __name__ == '__main__':
    get_file_names()
