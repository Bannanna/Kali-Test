from lib.kali import getkali
from lib.reqpks import gnuftp, parsehtml
from lib.tarutil import tarthem, unpackandinstall
# from lib.kali import *
# from lib.reqpks import *
# from lib.tarutil import *

#Step 1) -- get all available downloads from gnu.org
#Step 2) -- download all required packages -> save in downloads
#Step 3) -- use tar utils to install packages
#Step 4) -- download kali iso
#Step 5) -- use downloadsumsandverify to verify sums
#Step 6) -- TODO unit test above
#           TODO make functions for creating live usb <- unetbootin
#           TODO *check for downloads before downloading them

# all_routes, tar_routes, sig_routes = parsehtml.get_file_names()#G2G
# rec = tar_routes + sig_routes#G2G
# gnuftp.get_rec_files(recs=rec)#G2G
tarthem.config_make_install()
# getkali.getkali()
